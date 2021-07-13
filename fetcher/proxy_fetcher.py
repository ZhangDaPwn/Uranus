#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# @Time     : 2021/7/6 16:01
# @Author   : dapwn
# @File     : proxy_fetcher.py
# @Software : PyCharm

import re
import time
from time import sleep

from helper.spider_helper import RequestHandler


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
        url_list = [
            'http://www.kxdaili.com/dailiip/1/{page}.html',
            'http://www.kxdaili.com/dailiip/2/{page}.html'
        ]

        for base_url in url_list:
            for page in range(1, 11):
                url = base_url.format(page=page)
                try:
                    html_tree = RequestHandler().get(url).tree
                    trs = html_tree.xpath('//table[@class="active"]/tbody/tr')
                    for tr in trs:
                        ip = ''.join(tr.xpath('./td[1]/text()'))  # ip
                        port = ''.join(tr.xpath('./td[2]/text()'))  # 端口
                        anonymous = ''.join(tr.xpath('./td[3]/text()'))  # 匿名等級
                        proxy_type = ''.join(tr.xpath('./td[4]/text()'))  # 代理类型 HTTP/HTTPS/SOCKET
                        ping = ''.join(tr.xpath('./td[5]/text()'))  # 响应时间
                        region = ''.join(tr.xpath('./td[5]/text()'))  # 地理位置
                        if ip:
                            yield f'{ip}:{port}'
                except Exception as e:
                    print(e)
                time.sleep(1)

    @staticmethod
    def free_proxy_1():
        """
        网站：蜻蜓代理 url: https://proxy.horocn.com/free-china-proxy/all.html ip地区：国内 是否可选位置：否
        :return:
        """
        # 3218: data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD//gA7Q1JFQVRPUjogZ2QtanBlZyB2MS4wICh1c2luZyBJSkcgSlBFRyB2NjIpLCBxdWFsaXR5ID0gNTAK/9sAQwAQCwwODAoQDg0OEhEQExgoGhgWFhgxIyUdKDozPTw5Mzg3QEhcTkBEV0U3OFBtUVdfYmdoZz5NcXlwZHhcZWdj/9sAQwEREhIYFRgvGhovY0I4QmNjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2Nj/8AAEQgAMgBkAwEiAAIRAQMRAf/EAB8AAAEFAQEBAQEBAAAAAAAAAAABAgMEBQYHCAkKC//EALUQAAIBAwMCBAMFBQQEAAABfQECAwAEEQUSITFBBhNRYQcicRQygZGhCCNCscEVUtHwJDNicoIJChYXGBkaJSYnKCkqNDU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6g4SFhoeIiYqSk5SVlpeYmZqio6Slpqeoqaqys7S1tre4ubrCw8TFxsfIycrS09TV1tfY2drh4uPk5ebn6Onq8fLz9PX29/j5+v/EAB8BAAMBAQEBAQEBAQEAAAAAAAABAgMEBQYHCAkKC//EALURAAIBAgQEAwQHBQQEAAECdwABAgMRBAUhMQYSQVEHYXETIjKBCBRCkaGxwQkjM1LwFWJy0QoWJDThJfEXGBkaJicoKSo1Njc4OTpDREVGR0hJSlNUVVZXWFlaY2RlZmdoaWpzdHV2d3h5eoKDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uLj5OXm5+jp6vLz9PX29/j5+v/aAAwDAQACEQMRAD8A6miiigsKKKKACiiq99eR2Fq1xKrsqkDagySSccUgLFFY/wDwkUKAPcWV9bxH/lpJDhRWrHKksayRurI4yrA8EUAPooopgFFFFABRRRQAUUUUAZ94NVknKWjW0MIA/eOCzE+w6VSj1C/sdXgsdQaKZLgfu5Y12kH3Fa90s727rayLHMcbWZcgc+n0rnWE+na9bTasy3Xnfu4Zl+URn/d6d6liE8R2dzaac90dSupJN4AUNtUA+wrpLY77aJjzlAf0rK8XDOgTH0ZT+tF3rMWlaNaSMpeWWJfLXoCcDkn05oAk8T3gtNFnG5fMlGxVbvnrx9M1i6Vo+ny+HvtV4QshDES+YRsx04zinQRW9wZNT1S+trq4RCyWyyAquBkDHf6fzqbQtGsdT0/7ZdRh5pmb7h2BMHHAHHvRuBpeGHuZNFia7LFsnYW6le1a1YXhq5naS+sp5WmFpLtSRjkkZI6/hW7TQBRRRTGFFFFABRRRQBRvby8t5gsOnPcRlc70kA59MGs2W01DWb+2ku7cWlrbtvCFwzOfw+ldBRSEY2s2Gpaiktsktqlq+3G4Nv4wfp1FS6dY3sSpFfS288EcYRFWPkYxjk+wrUoosBTk0nT5fv2VuffywDVCPw/LatIthqU1tA5yY9obH0J6Vt0UWGU9N02DTIDHDuYsdzu5yzH3q5RRQAUUUUwCiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooA//2Q==
        # 3218: data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD//gA7Q1JFQVRPUjogZ2QtanBlZyB2MS4wICh1c2luZyBJSkcgSlBFRyB2NjIpLCBxdWFsaXR5ID0gNTAK/9sAQwAQCwwODAoQDg0OEhEQExgoGhgWFhgxIyUdKDozPTw5Mzg3QEhcTkBEV0U3OFBtUVdfYmdoZz5NcXlwZHhcZWdj/9sAQwEREhIYFRgvGhovY0I4QmNjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2Nj/8AAEQgAMgBkAwEiAAIRAQMRAf/EAB8AAAEFAQEBAQEBAAAAAAAAAAABAgMEBQYHCAkKC//EALUQAAIBAwMCBAMFBQQEAAABfQECAwAEEQUSITFBBhNRYQcicRQygZGhCCNCscEVUtHwJDNicoIJChYXGBkaJSYnKCkqNDU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6g4SFhoeIiYqSk5SVlpeYmZqio6Slpqeoqaqys7S1tre4ubrCw8TFxsfIycrS09TV1tfY2drh4uPk5ebn6Onq8fLz9PX29/j5+v/EAB8BAAMBAQEBAQEBAQEAAAAAAAABAgMEBQYHCAkKC//EALURAAIBAgQEAwQHBQQEAAECdwABAgMRBAUhMQYSQVEHYXETIjKBCBRCkaGxwQkjM1LwFWJy0QoWJDThJfEXGBkaJicoKSo1Njc4OTpDREVGR0hJSlNUVVZXWFlaY2RlZmdoaWpzdHV2d3h5eoKDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uLj5OXm5+jp6vLz9PX29/j5+v/aAAwDAQACEQMRAD8A66iiigQUVn6lfSwSRW9rGHnl6Z6AVVkvNT08rJeLHLCTglOoqlFsDaopFYMoYHIIyDS1IBRRRQAUUUA56UAFFFFABRRRQAUUUUAB6cda53U5NSuLb/SLXyoFO5ipyf51qalJeQiOW0XzFU/vIwOSKpz6ncXcLQW9jKHcFSWHC5q49wKusX63FvFBakmMIHf2HQA1u2b77GByesak/lWf/ZcdrpE42gzGE72HfHNWdFbzNJgzzgFT+BNErW0ApC81HUZXNgUigQ4DMPvfoamsb+5W9+xX6ASkZR1/iq/JJBZwl22RRjngY5rJtTJqmrreCMpbwjCk9+v+NGjWwDr8Ne6wli8jRwhNxAONxqOaD+yL+2NtI5SZtrRsc56f40SRyazqEmxlhjtjtDgfMT/kUw276bqlvJdOblZDtV2Jyp/yapdgOhooorIAooooAKKKKACiiigBsi742Q/xAis6win07SnEke+RCSqIc5rTop36Acq08k9152pQTuq/djVSAK2tP1OC6k+zxQyRlVzggAAVoUVTkn0AyJrC7truS4090xKcvG/rRFY3t1dxz6gyBYjlY09a16KXMwCiiipAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigD/2Q==
        # 3218: data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD//gA7Q1JFQVRPUjogZ2QtanBlZyB2MS4wICh1c2luZyBJSkcgSlBFRyB2NjIpLCBxdWFsaXR5ID0gNTAK/9sAQwAQCwwODAoQDg0OEhEQExgoGhgWFhgxIyUdKDozPTw5Mzg3QEhcTkBEV0U3OFBtUVdfYmdoZz5NcXlwZHhcZWdj/9sAQwEREhIYFRgvGhovY0I4QmNjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2Nj/8AAEQgAMgBkAwEiAAIRAQMRAf/EAB8AAAEFAQEBAQEBAAAAAAAAAAABAgMEBQYHCAkKC//EALUQAAIBAwMCBAMFBQQEAAABfQECAwAEEQUSITFBBhNRYQcicRQygZGhCCNCscEVUtHwJDNicoIJChYXGBkaJSYnKCkqNDU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6g4SFhoeIiYqSk5SVlpeYmZqio6Slpqeoqaqys7S1tre4ubrCw8TFxsfIycrS09TV1tfY2drh4uPk5ebn6Onq8fLz9PX29/j5+v/EAB8BAAMBAQEBAQEBAQEAAAAAAAABAgMEBQYHCAkKC//EALURAAIBAgQEAwQHBQQEAAECdwABAgMRBAUhMQYSQVEHYXETIjKBCBRCkaGxwQkjM1LwFWJy0QoWJDThJfEXGBkaJicoKSo1Njc4OTpDREVGR0hJSlNUVVZXWFlaY2RlZmdoaWpzdHV2d3h5eoKDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uLj5OXm5+jp6vLz9PX29/j5+v/aAAwDAQACEQMRAD8A7eiiisiQooooAKKCQBknAFVLTUYLyaWOEsfL6sRwfpRcdi3RTHmiRwjyorHoCwBNZU1/fXF5LBp8SFYTh2f1pN2BJs2KKo6VftexyLKgSaJtrgdP88Gr1NO4NW0CiiigQUUUUAFFFFABUN1cxWkDTTNhR+ZPpU1Q3NrDdIqzpvVW3AZ70PyGvMzk1a0v82sySRCUYBbjOfeotIhW31e8gj4VVGM81Fqd0mpXMNlboyyLJy7DGMen+e1T27rD4hvmdgqiMMSe33azvqaWsgbRIFt5pb2YvKcsZc4xWXpFte3MkjWsxiAGHfPWtEmXXbjA3R2MZ5PdzTvst7pdzI9hEs0EhzsJ5WlZXuthptKz3E0zzNMvzZ3AVjP8yyg9T71uVkWlpd3N+t7fqsfljEcYrXq47ET3CiiiqICiiigAooooAKoarc3FmsU0S7olb96MZOKv0UMa0OfuLlNV1G0FnG26NtzyEYwMitm5tILqN0lQYfGSOCcdOalVFQYVQv0GKdSS7jcuxkHw9bqcwzzRn2IrViTy4kTcW2gDc3U+5p1FCSWwnJvcKKKKYgooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigD//2Q==

        # 80：  data:image/jpeg;base64,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
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
    for proxy in ProxyFetcher.free_proxy_0():
        print(proxy)
