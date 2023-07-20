import requests
import urllib3
from pyquery import PyQuery as pq
from proxypool.schemas.proxy import Proxy
from proxypool.crawlers.base import BaseCrawler
import re

urllib3.disable_warnings()
BASE_URL = 'https://proxy.seofangfa.com/'
MAX_PAGE = 1


class SeoFangFaCrawler(BaseCrawler):
    """
    seo方法 crawler, https://proxy.seofangfa.com/
    """
    urls = [BASE_URL]

    def parse(self, html):
        """
        parse html file to get proxies
        :return:
        """
        doc = pq(html)
        trs = doc('.table tr:gt(0)').items()
        for tr in trs:
            host = tr.find('td:nth-child(1)').text()
            port = tr.find('td:nth-child(2)').text()
            yield Proxy(host=host, port=port)


if __name__ == '__main__':
    crawler = SeoFangFaCrawler()
    for proxy in crawler.crawl():
        print(proxy)
