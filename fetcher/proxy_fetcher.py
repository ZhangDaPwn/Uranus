#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# @Time     : 2021/7/6 16:01
# @Author   : dapwn
# @File     : proxy_fetcher.py
# @Software : PyCharm

import re
from time import sleep

from Uranus.helper.spider_helper import RequestHandler


class ProxyFetcher(object):
    """
    proxy getter
    """

    @staticmethod
    def free_proxy_0():
        """
        网站：开心代理 url: http://www.kxdaili.com/dailiip.html ip地区：国内 是否可选位置：否
        :return:
        """
        yield ''

    @staticmethod
    def free_proxy_1():
        """
        网站：蜻蜓代理 url: https://proxy.horocn.com/free-china-proxy/all.html ip地区：国内 是否可选位置：否
        :return:
        """
        yield ''

    @staticmethod
    def free_proxy_2():
        """
        网站：米扑代理 url: https://proxy.mimvp.com/freeopen ip地区：全球 是否可选位置：国内/国外
        状态：游客和无登录，只能获取第一页数据，pass
        :return:
        """
        url_list = [
            'https://proxy.mimvp.com/freeopen',
            'https://proxy.mimvp.com/freeopen?proxy=in_tp',
            'https://proxy.mimvp.com/freeopen?proxy=in_tp',
            'https://proxy.mimvp.com/freeopen?proxy=out_hp',
            'https://proxy.mimvp.com/freeopen?proxy=out_tp'
        ]
        # 因为代理端口号是图片，根据图片地址，枚举出对应的值，可能不全
        port_img_map = {
            'Dgw': '80',
            'DgwOA': '808',
            'DMxMjg': '3128',
            'DgwMDA': '8000',
            'DgwODA': '8080',
            'DgwODE': '8081',
            'Dg4ODg': '8888',
            'Dk5OTk': '9999',
            'DM5ODQ2': '39846',
        }
        for url in url_list:
            html_tree = RequestHandler().get(url=url).tree
            trs = html_tree.xpath('.//table[@class="mimvp-tbl free-proxylist-tbl"]/tbody/tr')
            for tr in trs:
                try:
                    ip = ''.join(tr.xpath('./td[2]/text()'))
                    port_img = ''.join(tr.xpath('./td[3]/img/@src')).split("port=")[-1]
                    port = port_img_map.get(port_img[14:].replace('O0O', ''))
                    if port:
                        yield '{}:{}'.format(ip, port)
                except Exception as e:
                    print("free_proxy_2: error: ", str(e))

    @staticmethod
    def free_proxy_3():
        """
        网站：ProxyScan url: https://www.proxyscan.io ip地区：全球 是否可选位置：是
        :return:
        """
        yield ''

    @staticmethod
    def free_proxy_4():
        """
        网站：ProxyList url: https://www.proxy-list.download/HTTP ip地区：全球 是否可选位置：是
        :return:
        """
        yield ''

    @staticmethod
    def free_proxy_5():
        """
        网站：ProxyDB url: http://proxydb.net ip地区：全球 是否可选位置：是
        :return:
        """
        yield ''

    @staticmethod
    def free_proxy_6():
        """
        网站：FreeProxy url: http://free-proxy.cz ip地区：全球 是否可选位置：是
        :return:
        """
        yield ''

    @staticmethod
    def free_proxy_7():
        """
        网站：Spys url: https://spys.one ip地区：全球 是否可选位置：是
        :return:
        """
        yield ''

    @staticmethod
    def free_proxy_8():
        """
        网站：PremProxy url: https://premproxy.com/list ip地区：全球 是否可选位置：是
        :return:
        """
        yield ''

    @staticmethod
    def free_proxy_9():
        """
        网站：FreeProxyList url: https://free-proxy-list.net ip地区：全球 是否可选位置：是
        :return:
        """
        yield ''

    @staticmethod
    def free_proxy_10():
        """
        网站：ProxyNova url: https://www.proxynova.com/proxy-server-list ip地区：全球 是否可选位置：是
        :return:
        """
        yield ''


if __name__ == '__main__':
    for proxy in ProxyFetcher.free_proxy_2():
        print(proxy)
