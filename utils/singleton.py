#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# @Time     : 2021/7/7 9:48
# @Author   : dapwn
# @File     : singleton.py
# @Software : PyCharm
"""
-------------------------------------------------
   Description :   单元集
   Author :        dapwn
   date：          2021/7/7
-------------------------------------------------
   Point:
-------------------------------------------------
"""
__author__ = 'dapwn'


class Singleton(type):
    """
    Singleton Metaclass
    """

    _inst = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._inst:
            cls._inst[cls] = super(Singleton, cls).__call__(*args)
        return cls._inst[cls]
