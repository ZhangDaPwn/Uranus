#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# @Time     : 2021/7/7 10:51
# @Author   : dapwn
# @File     : config_handler.py
# @Software : PyCharm
"""
-------------------------------------------------
   Description :
   Author :        dapwn
   date：          2021/7/7
-------------------------------------------------
   point:
-------------------------------------------------
"""
__author__ = 'dapwn'

import os
import settings
from utils.six import reload_six, with_metaclass
from utils.singleton import Singleton
from utils.lazy_property import LazyProperty


class ConfigHandler(with_metaclass(Singleton)):

    def __init__(self):
        pass

    @LazyProperty
    def server_host(self):
        return os.environ.get("HOST", settings.HOST)

    @LazyProperty
    def server_port(self):
        return os.environ.get("PORT", settings.PORT)

    @LazyProperty
    def db_conn(self):
        return os.getenv("DB_CONN", settings.DB_CONN)

    @LazyProperty
    def table_name(self):
        return os.getenv("TABLE_NAME", settings.TABLE_NAME)

    @LazyProperty
    def fetchers(self):
        reload_six(settings)
        return settings.PROXY_FETCHER

    @LazyProperty
    def http_url(self):
        return os.getenv("HTTP_URL", settings.HTTP_URL)

    @LazyProperty
    def https_url(self):
        return os.getenv("HTTPS_URL", settings.HTTPS_URL)

    @LazyProperty
    def verify_timeout(self):
        return os.getenv("VERIFY_TIMEOUT", settings.VERIFY_TIMEOUT)

    # @LazyProperty
    # def proxy_check_count(self):
    #     return os.getenv("PROXY_CHECK_COUNT", settings.PROXY_CHECK_COUNT)

    @LazyProperty
    def max_fail_count(self):
        return os.getenv("MAX_FAIL_COUNT", settings.MAX_FAIL_COUNT)

    # @LazyProperty
    # def max_fail_rate(self):
    #     return os.getenv("MAX_FAIL_RATE", settings.MAX_FAIL_RATE)

    @LazyProperty
    def pool_size_min(self):
        return os.getenv("POOL_SIZE_MIN", settings.POOL_SIZE_MIN)

    @LazyProperty
    def timezone(self):
        return os.getenv("TIMEZONE", settings.TIMEZONE)

    @LazyProperty
    def thread_num(self):
        return os.getenv("THREAD_NUM", settings.THREAD_NUM)
