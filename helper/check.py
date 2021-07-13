#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# @Time     : 2021/7/7 15:44
# @Author   : dapwn
# @File     : check.py
# @Software : PyCharm
"""
-------------------------------------------------
   Description :   校验代理
   Author :        dapwn
   date：          2021/7/7
-------------------------------------------------
   point:
-------------------------------------------------
"""
__author__ = 'dapwn'

from utils.six import Empty
from threading import Thread
from datetime import datetime
from handler.log_handler import LogHandler
from helper.validator import ProxyValidator
from handler.proxy_handler import ProxyHandler
from handler.config_handler import ConfigHandler


class DoValidator(object):
    """执行校验"""

    @classmethod
    def validator(cls, proxy):
        """
        校验入口
        Args:
            proxy: Proxy Object
        Returns:
            Proxy Object
        """
        http_resp = cls.http_validator(proxy)
        https_resp = False if not http_resp else cls.https_validator(proxy)

        proxy.check_count += 1
        proxy.last_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        proxy.last_status = True if http_resp else False
        if http_resp:
            if proxy.fail_count > 0:
                proxy.fail_count -= 1
            proxy.https = True if https_resp else False
        else:
            proxy.fail_count += 1
        return proxy

    @classmethod
    def http_validator(cls, proxy):
        for func in ProxyValidator.http_validator:
            if not func(proxy.proxy):
                return False
        return True

    @classmethod
    def https_validator(cls, proxy):
        for func in ProxyValidator.https_validator:
            if not func(proxy.proxy):
                return False
        return True

    @classmethod
    def pre_validator(cls, proxy):
        for func in ProxyValidator.pre_validator:
            if not func(proxy):
                return False
        return True


class _ThreadChecker(Thread):
    """多线程检测"""

    def __init__(self, work_type, target_queue, thread_name):
        Thread.__init__(self, name=thread_name)
        self.work_type = work_type
        self.log = LogHandler("checker")
        self.proxy_handler = ProxyHandler()
        self.target_queue = target_queue
        self.conf = ConfigHandler()

    def run(self):
        self.log.info("{}ProxyCheck - {}: start".format(self.work_type.title(), self.name))
        while True:
            try:
                proxy = self.target_queue.get(block=False)
            except Empty:
                self.log.info("{}ProxyCheck - {}: complete".format(self.work_type.title(), self.name))
                break
            proxy = DoValidator.validator(proxy)
            if self.work_type == "raw":
                self.__is_raw(proxy)
            else:
                self.__is_use(proxy)
            self.target_queue.task_done()

    def __is_raw(self, proxy):
        if proxy.last_status:
            if self.proxy_handler.exists(proxy):
                self.log.info('RawProxyCheck - {}: {} exist'.format(self.name, proxy.proxy.ljust(23)))
            else:
                self.log.info('RawProxyCheck - {}: {} pass'.format(self.name, proxy.proxy.ljust(23)))
                self.proxy_handler.put(proxy)
        else:
            self.log.info('RawProxyCheck - {}: {} fail'.format(self.name, proxy.proxy.ljust(23)))

    def __is_use(self, proxy):
        if proxy.last_status:
            self.log.info('UseProxyCheck - {}: {} pass'.format(self.name, proxy.proxy.ljust(23)))
            self.proxy_handler.put(proxy)
        else:
            if proxy.fail_count > self.conf.max_fail_count:
                self.log.info('UseProxyCheck - {}: {} fail, count {} delete'.format(self.name,
                                                                                    proxy.proxy.ljust(23),
                                                                                    proxy.fail_count))
                self.proxy_handler.delete(proxy)
            else:
                self.log.info('UseProxyCheck - {}: {} fail, count {} keep'.format(self.name,
                                                                                  proxy.proxy.ljust(23),
                                                                                  proxy.fail_count))
                self.proxy_handler.put(proxy)


def Checker(tp, queue):
    """
    run Proxy ThreadChecker
    :param tp: raw/use
    :param queue: Proxy Queue
    :return:
    """
    conf = ConfigHandler()
    thread_list = list()
    for index in range(conf.thread_num):
        thread_list.append(_ThreadChecker(tp, queue, "htead_%s" % str(index).zfill(2)))

    for thread in thread_list:
        thread.setDaemon(True)
        thread.start()

    for thread in thread_list:
        thread.join()
