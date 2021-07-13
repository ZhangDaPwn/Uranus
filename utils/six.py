#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# @Time     : 2021/7/7 9:20
# @Author   : dapwn
# @File     : six.py
# @Software : PyCharm
"""
-------------------------------------------------
   Description :   用来兼容python2和python3双环境的工具类
   Author :        dapwn
   date：          2021/7/7
-------------------------------------------------
   Point:
   from collections import Iterable
   isinstance(object,Iterable)  # 判断是否为支持可迭代对象

   iter(object[, sentinel])  # 迭代生成器

   reload: 用于重新载入之前的模块
-------------------------------------------------
"""
__author__ = 'dapwn'

import sys

Python3 = sys.version_info[0] == 3

if Python3:
    def iteritems(d, **kwargs):
        return iter(d.items(**kwargs))
else:
    def iteritems(d, **kwargs):
        return d.iteritems(**kwargs)

if Python3:
    from urllib.parse import urlparse
else:
    from urlparse import urlparse

if Python3:
    from imp import reload as reload_six
else:
    reload_six = reload

if Python3:
    from queue import Empty, Queue
else:
    from Queue import Empty, Queue


def with_metaclass(meta, *bases):
    """
    Create a base class with a metaclass
    This requires a bit of explanation:
    the basic idea is to make a dummy metaclass for one level of class instantiation that replaces itself with the actual metaclass.
    """

    class MetaClass(meta):

        def __new__(cls, name, this_bases, d):
            return meta(name, bases, d)

    return type.__new__(MetaClass, 'temporary_class', (), {})
