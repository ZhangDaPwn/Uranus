#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# @Time     : 2021/7/7 15:33
# @Author   : dapwn
# @File     : fetch.py
# @Software : PyCharm
"""
-------------------------------------------------
   Description :   爬取
   Author :        dapwn
   date：          2021/7/7
-------------------------------------------------
   point:
   callable: 检测一个函数是否可以调用， 返回 True/False
-------------------------------------------------
"""
__author__ = 'dapwn'

from helper.proxy import Proxy
from helper.check import DoValidator
from handler.log_handler import LogHandler
from handler.config_handler import ConfigHandler
from handler.proxy_handler import ProxyHandler
from fetcher.proxy_fetcher import ProxyFetcher


class Fetcher(object):
    name = "fetcher"

    def __init__(self):
        self.log = LogHandler(self.name)
        self.conf = ConfigHandler()
        self.proxy_handler = ProxyHandler()

    def run(self):
        """
        fetch proxy with ProxyFetcher
        :return:
        """
        proxy_dict = dict()
        self.log.info("ProxyFetch : start")
        for fetch_source in self.conf.fetchers:
            self.log.info("ProxyFetch - {func}: start".format(func=fetch_source))
            fetcher = getattr(ProxyFetcher, fetch_source, None)
            if not fetcher:
                self.log.error("ProxyFetch - {func}: class method not exists!".format(func=fetch_source))
                continue
            if not callable(fetcher):
                self.log.error("ProxyFetch - {func}: must be class method".format(func=fetch_source))
                continue

            try:
                for proxy in fetcher():
                    self.log.info("ProxyFetch - %s: %s ok" % (fetch_source, proxy.ljust(23),))
                    proxy = proxy.strip()
                    if proxy in proxy_dict:
                        proxy_dict[proxy].add_source(fetch_source)
                    else:
                        proxy_dict[proxy] = Proxy(proxy, source=fetch_source)
            except Exception as e:
                self.log.error("ProxyFetch - {func}: error".format(func=fetch_source))
                self.log.error(str(e))
        self.log.info("ProxyFetch - all complete!")
        for _ in proxy_dict.values():
            if DoValidator.pre_validator(_.proxy):
                yield _



