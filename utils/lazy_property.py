#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# @Time     : 2021/7/7 11:15
# @Author   : dapwn
# @File     : lazy_property.py
# @Software : PyCharm
"""
-------------------------------------------------
   Description :   延迟初始化：当它第一次被创建时才进行初始化，或者保存第一次创建结果，以后每次用的时候直接返回该结果，提高计算性能，减少计算资源浪费
   Author :        dapwn
   date：          2021/7/7
-------------------------------------------------
   point:
-------------------------------------------------
"""
__author__ = 'dapwn'


class LazyProperty(object):

    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value
