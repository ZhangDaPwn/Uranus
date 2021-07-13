#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# @Time     : 2021/7/6 14:25
# @Author   : dapwn
# @File     : settings.py
# @Software : PyCharm

BANNER = r"""
      ___           ___           ___           ___           ___           ___     
     /__/\         /  /\         /  /\         /__/\         /__/\         /  /\    
     \  \:\       /  /::\       /  /::\        \  \:\        \  \:\       /  /:/_   
      \  \:\     /  /:/\:\     /  /:/\:\        \  \:\        \  \:\     /  /:/ /\  
  ___  \  \:\   /  /:/ /:/    /  /:/ /::\   _____\__\:\   ___  \  \:\   /  /:/ /::\ 
 /__/\  \__\:\ /__/:/ /:/___ /__/:/ /:/\:\ /__/::::::::\ /__/\  \__\:\ /__/:/ /:/\:\
 \  \:\ /  /:/ \  \:\/:::::/ \  \:\/:/__\/ \  \:\--\--\/ \  \:\ /  /:/ \  \:\/:/ /:/
  \  \:\  /:/   \  \::/````   \  \::/       \  \:\        \  \:\  /:/   \  \::/ /:/ 
   \  \:\/:/     \  \:\        \  \:\        \  \:\        \  \:\/:/     \__\/ /:/  
    \  \::/       \  \:\        \  \:\        \  \:\        \  \::/        /__/:/   
     \__\/         \__\/         \__\/         \__\/         \__\/         \__\/    
"""
# banner 生成地址：http://www.network-science.de/ascii/  Font：isometric3

VERSION = "1.0.0"

# ############### server config ###############
HOST = "0.0.0.0"

PORT = 4399

# ############### database config ###################
# db connection uri
# example:
#      Redis: redis://:password@ip:port/db
#      Ssdb:  ssdb://:password@ip:port
DB_CONN = 'redis://:vango123@127.0.0.1:6379/0'

# proxy table name
TABLE_NAME = 'use_proxy'

# ###### config the proxy fetch function ######
PROXY_FETCHER = [
    "free_proxy_0",
    # "free_proxy_1",
    "free_proxy_2",
    # "free_proxy_3",
    # "free_proxy_4",
    # "free_proxy_5",
    # "free_proxy_6",
    # "free_proxy_7",
    # "free_proxy_8",
    # "free_proxy_9",
    # "free_proxy_10"
]

# ############# proxy validator #################
# 代理验证目标网站
HTTP_URL = "http://httpbin.org"

HTTPS_URL = "https://www.qq.com"

# 代理验证时超时时间
VERIFY_TIMEOUT = 10

# 近PROXY_CHECK_COUNT次校验中允许的最大失败次数,超过则剔除代理
MAX_FAIL_COUNT = 0

# 近PROXY_CHECK_COUNT次校验中允许的最大失败率,超过则剔除代理
# MAX_FAIL_RATE = 0.1

# proxyCheck时代理数量少于POOL_SIZE_MIN触发抓取
POOL_SIZE_MIN = 20

TIMEZONE = "Asia/Shanghai"

# 多线程检测代理，线程数
THREAD_NUM = 20



















# 免费代理网站列表
# 不翻墙可正常访问的网站：
FREE_PROXY_URL_0 = 'http://www.kxdaili.com/dailiip.html'                 # 网站：开心代理       ip地区：国内 是否可选位置：否
FREE_PROXY_URL_1 = 'https://proxy.horocn.com/free-china-proxy/all.html'  # 网站：蜻蜓代理       ip地区：国内 是否可选位置：否
FREE_PROXY_URL_2 = 'https://proxy.mimvp.com/freeopen'                    # 网站：米扑代理       ip地区：全球 是否可选位置：国内/国外
FREE_PROXY_URL_3 = 'https://www.proxyscan.io'                            # 网站：ProxyScan     ip地区：全球 是否可选位置：是
FREE_PROXY_URL_4 = 'https://www.proxy-list.download/HTTP'                # 网站：ProxyList     ip地区：全球 是否可选位置：是
FREE_PROXY_URL_5 = 'http://proxydb.net'                                  # 网站：ProxyDB       ip地区：全球 是否可选位置：是

# 需翻墙的网站：
FREE_PROXY_URL_6 = 'http://free-proxy.cz'                                # 网站：FreeProxy     ip地区：全球 是否可选位置：是
FREE_PROXY_URL_7 = 'https://spys.one'                                    # 网站：Spys          ip地区：全球 是否可选位置：是
FREE_PROXY_URL_8 = 'https://premproxy.com/list'                          # 网站：PremProxy     ip地区：全球 是否可选位置：否
FREE_PROXY_URL_9 = 'https://free-proxy-list.net'                         # 网站：FreeProxyList ip地区：全球 是否可选位置：是
FREE_PROXY_URL_10 = 'https://www.proxynova.com/proxy-server-list'        # 网站：ProxyNova     ip地区：全球 是否可选位置：是
