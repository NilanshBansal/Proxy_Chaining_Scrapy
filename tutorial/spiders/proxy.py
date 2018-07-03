
import scrapy
import random
from scrapy.http.request import Request


class ProxySpider(scrapy.Spider):
    name = 'proxy'
    allowed_domains = ['8e7e2b0b.ngrok.io']
    start_urls = ['https://8e7e2b0b.ngrok.io/']

    def __init__(self, *args, **kwargs):
        self.logger.info('CALLING CONSTRUCTOR!!!!!!!!')
        super(ProxySpider, self).__init__(*args, **kwargs)
        self.proxy_pool = ['200.255.122.174:8080', '175.196.224.242:8080', '80.150.65.6:808',
                           '81.211.3.114:8080', '182.74.34.134:8080', '45.113.66.33:8080', '115.178.99.91:53281']

    def parse(self, response):
        self.logger.info("I just visited : " + response.url)
        request = Request(url="https://8e7e2b0b.ngrok.io")
        request.meta['proxy'] = random.choice(self.proxy_pool)
        self.log(request)
        yield request
