#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# @Time     : 2021/7/6 16:02
# @Author   : dapwn
# @File     : spider_helper.py
# @Software : PyCharm
'''
@property:将方法名转成可读的属性
return self  # 链式调用
'''
__author__ = 'dapwn'

from requests.models import Response
from lxml import etree
import requests
import random
import time

from ..handler.log_handler import LogHandler

requests.packages.urllib3.disable_warnings()  # 屏蔽https证书警告


class RequestHandler(object):
    name = 'request_handler'

    def __init__(self, *args, **kwargs):
        self.log = LogHandler(self.name, file=False)
        self.response = Response()

    @property
    def user_agent(self):
        """
        return an User-Agent at random
        :return:
        """
        ua_list = [
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
            'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
        ]
        return random.choice(ua_list)

    @property
    def headers(self):
        """
        basic headers
        :return:
        """
        return {
            'User-Agent': self.user_agent,
            'Accept': '*/*',
            'Connection': 'keep-alive',
        }

    def get(self, url, header=None, retry_times=3, retry_interval=5, timeout=5, *args, **kwargs):
        """
        Method: GET
        :param url: target url
        :param header: header
        :param retry_times: retry time
        :param retry_interval: retry interval
        :param timeout: max request time
        :param args:
        :param kwargs:
        :return:
        """
        headers = self.headers
        if headers and isinstance(header, dict):
            headers.update(header)
        while True:
            try:
                self.response = requests.get(url, headers=headers, timeout=timeout, *args, **kwargs)
                return self  # 链式调用
            except Exception as e:
                self.log.error("requests: %s error: %s" % (url, str(e)))
                retry_times -= 1
                if retry_times <= 0:
                    resp = Response()
                    resp.status_code = 200
                    return self
                self.log.info("retry %s second after" % retry_interval)
                time.sleep(retry_interval)

    @property
    def tree(self):
        return etree.HTML(self.response.content)

    @property
    def text(self):
        return self.response.text

    @property
    def json(self):
        try:
            return self.response.json()
        except Exception as e:
            self.log.error(str(e))
            return {}
