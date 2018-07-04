# -*- coding: utf-8 -*-
import scrapy
import random
from scrapy.http.request import Request


class ProxySpider(scrapy.Spider):
    name = 'proxy'
    # allowed_domains = ['8e7e2b0b.ngrok.io']
    start_urls = []

    def __init__(self, *args, **kwargs):
        super(ProxySpider, self).__init__(*args, **kwargs)
        self.proxy_pool = ['103.23.134.106:8080', '79.143.112.11:8080', '91.238.28.124:8080', '93.87.25.130:8080', '90.179.167.133:8080', '99.255.104.123:8080', '83.234.120.180:8080', '91.210.178.161:8080', '183.88.63.126:8080', '59.106.222.74:60088', '89.37.194.133:8080', '85.196.145.18:8080', '94.21.243.77:8080', '23.100.105.68:3128', '67.43.113.218:8080', '91.193.237.202:53281', '43.249.142.14:8080', '140.227.74.74:3128', '140.227.81.53:3128', '103.79.235.22:8080', '91.227.47.19:8080']

    def start_requests(self):
        request = Request(url="https://b48f921d.ngrok.io")
        # request.meta['proxy'] = random.choice(self.proxy_pool)
        self.logger.info('i am visiting url ')
        yield request

    
    def parse(self, response):  
        self.logger.info('DEKH BHAI DEKH')
        pass
