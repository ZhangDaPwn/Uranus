#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# @Time     : 2021/7/7 15:47
# @Author   : dapwn
# @File     : validator.py
# @Software : PyCharm
"""
-------------------------------------------------
   Description :   定义代理检验方法
   Author :        dapwn
   date：          2021/7/7
-------------------------------------------------
   point:
-------------------------------------------------
"""
__author__ = 'dapwn'

import re
import requests
from utils.six import with_metaclass
from utils.singleton import Singleton
from handler.config_handler import ConfigHandler

conf = ConfigHandler()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
    'Accept': '*/*',
    'Connection': 'keep-alive',
}


class ProxyValidator(with_metaclass(Singleton)):
    pre_validator = []
    http_validator = []
    https_validator = []

    @classmethod
    def add_pre_validator(cls, func):
        cls.pre_validator.append(func)

    @classmethod
    def add_http_validator(cls, func):
        cls.http_validator.append(func)

    @classmethod
    def add_https_validator(cls, func):
        cls.https_validator.append(func)


@ProxyValidator.add_pre_validator
def format_validator(proxy):
    """检查代理格式"""
    verify_regex = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}"
    _proxy = re.findall(verify_regex, proxy)
    return True if len(_proxy) == 1 and _proxy[0] == proxy else False


@ProxyValidator.add_https_validator
def https_timeout_validator(proxy):
    """https检测超时"""
    proxies = {
        "http": "http://{proxy}".format(proxy=proxy),
        "https": "https://{proxy}".format(proxy=proxy),
    }
    try:
        resp = requests.head(url=conf.https_url, headers=headers, proxies=proxies, timeout=conf.verify_timeout,
                             verify=False)
        return True if resp.status_code == 200 else False
    except Exception as e:
        return False


@ProxyValidator.add_http_validator
def custom_validator_example(proxy):
    """自定义validator函数，校验代理是否可用, 返回True/False"""
    return True
