# -*- coding: utf-8 -*-
import scrapy


class JobbleSpider(scrapy.Spider):
    name = 'jobble'
    allowed_domains = ['blog.jobble.com']
    start_urls = ['http://blog.jobble.com/']

    def parse(self, response):
        print(response)
        pass
