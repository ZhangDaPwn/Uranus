#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# @Time     : 2021/7/7 9:09
# @Author   : dapwn
# @File     : launcher.py
# @Software : PyCharm
"""
-------------------------------------------------
   Description :   启动器
   Author :        dapwn
   date：          2021/7/7
-------------------------------------------------
   Point:
-------------------------------------------------
"""
__author__ = 'dapwn'

import sys
from db.db_client import DatabaseClient
from handler.log_handler import LogHandler
from handler.config_handler import ConfigHandler

log = LogHandler('launcher')


def start_server():
    __before_start()
    from api.proxy_api import run_flask
    run_flask()


def start_scheduler():
    __before_start()
    from helper.scheduler import run_scheduler
    run_scheduler()


def __before_start():
    __show_version()
    __show_config()
    if __check_database_config():
        log.info('exit!')
        sys.exit()


def __show_version():
    from settings import VERSION
    log.info("Uranus Version: %s" % VERSION)


def __show_config():
    conf = ConfigHandler()
    log.info("Uranus HOST: %s" % conf.server_host)
    log.info("Uranus PORT: %s" % conf.server_port)
    log.info("Uranus DB_CONN: %s" % conf.db_conn)
    log.info("Uranus PROXY_FETCHER: %s" % conf.fetchers)


def __check_database_config():
    conf = ConfigHandler()
    db = DatabaseClient(conf.db_conn)
    log.info("============ DATABASE CONFIGURE ================")
    log.info("DB_TYPE: %s" % db.db_type)
    log.info("DB_HOST: %s" % db.db_host)
    log.info("DB_PORT: %s" % db.db_port)
    log.info("DB_NAME: %s" % db.db_name)
    log.info("DB_USER: %s" % db.db_user)
    log.info("=================================================")
    return db.test()
