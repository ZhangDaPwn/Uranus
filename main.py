#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# @Time     : 2021/7/7 8:58
# @Author   : dapwn
# @File     : main.py
# @Software : PyCharm
"""
-------------------------------------------------
   Description :   Uranus 启动入口
   Author :        dapwn
   date：          2021/7/7
-------------------------------------------------
   Point:
   click: 用于快速创建命令行
-------------------------------------------------
"""
__author__ = 'dapwn'

import click
from helper.launcher import start_server, start_scheduler
from settings import BANNER, VERSION

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option(version=VERSION)
def cli():
    """Uranus cli 工具"""


@cli.command(name="schedule")
def schedule():
    """启动调度程序"""
    click.echo(BANNER)
    start_scheduler()


@cli.command(name="server")
def server():
    """启动api服务"""
    click.echo(BANNER)
    start_server()


if __name__ == '__main__':
    cli()
