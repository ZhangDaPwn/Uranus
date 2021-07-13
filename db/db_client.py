#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# @Time     : 2021/7/7 9:14
# @Author   : dapwn
# @File     : db_client.py
# @Software : PyCharm
"""
-------------------------------------------------
   Description :   DB工厂类
   Author :        dapwn
   date：          2021/7/7
-------------------------------------------------
   Point:
   urlparse: 解析出url的协议，域名服务器，路径等
   assert: 断言 用于判断一个表达式，在条件为false触发，断言可以在条件不满足程序运行条件时直接返回，而不必等程序崩溃后再返回
   getattr: 用于返回一个对象的属性值，当调用不存在的方法或者属性时，直接返回getattr的返回值
-------------------------------------------------
"""
__author__ = 'dapwn'

import os
import sys

from utils.six import urlparse, with_metaclass
from utils.singleton import Singleton

sys.path.append(os.path.dirname(os.path.abspath(__file__)))  # 将当前文件路径添加到sys系统路径中


class DatabaseClient(with_metaclass(Singleton)):
    """
    DatabaseClient DB工厂类
    提供get/put/update/pop/delete/exists/get_all/clean/get_count/change_table等方法

    抽象方法定义：
        get(): 随机返回一个proxy
        put(proxy): 存入一个proxy
        pop(): 顺序返回并删除一个proxy
        update(proxy): 更新指定proxy信息
        delete(proxy): 删除指定proxy
        exists(proxy): 判断指定proxy是否存在
        get_all(): 返回所有proxy信息
        clean(): 清除所有proxy信息
        get_count(): 返回proxy统计信息
        change_table(name): 切换操作对象

        所有方法需要对应类去具体实现：
            redis: redis_client.py
            mysql: mysql_client.py
            mongodb: mongodb_client.py
            ssdb: ssdb_client.py
    """

    def __init__(self, db_conn):
        """
        init
        :param db_conn:
        """
        self.parse_db_conn(db_conn)
        self.__init_db_client()

    @classmethod
    def parse_db_conn(cls, db_conn):
        db_conf = urlparse(db_conn)
        cls.db_type = db_conf.scheme.upper().strip()  # 解析url协议类型并转化成大写
        cls.db_host = db_conf.hostname
        cls.db_port = db_conf.port
        cls.db_user = db_conf.username
        cls.db_pwd = db_conf.password
        cls.db_name = db_conf.path[1:]
        return cls

    def __init_db_client(self):
        """
        init database client
        :return:
        """
        __type = None
        if "REDIS" == self.db_type:
            __type = "redis_client"
        elif "MYSQL" == self.db_type:
            __type = "mysql_client"
        elif "MONGODB" == self.db_type:
            __type = "mongodb_client"
        elif "SSDB" == self.db_type:
            __type = "ssdb_client"
        else:
            pass
        assert __type, 'type error, not support DB type:{}'.format(self.db_type)
        self.client = getattr(__import__(__type), "%sClient" % self.db_type.title())(
            host=self.db_host,
            port=self.db_port,
            username=self.db_user,
            password=self.db_pwd,
            db=self.db_name
        )

    def get(self, https, **kwargs):
        return self.client.get(https, **kwargs)

    def put(self, key, **kwargs):
        return self.client.put(key, **kwargs)

    def update(self, key, value, **kwargs):
        return self.client.update(key, value, **kwargs)

    def delete(self, key, **kwargs):
        return self.client.delete(key, **kwargs)

    def exists(self, key, **kwargs):
        return self.client.exists(key, **kwargs)

    def pop(self, https, **kwargs):
        return self.client.pop(https, **kwargs)

    def get_all(self, https):
        return self.client.get_all(https)

    def clear(self):
        return self.client.clear()

    def change_table(self, name):
        self.client.change_table(name)

    def get_count(self):
        return self.client.get_count()

    def test(self):
        return self.client.test()
