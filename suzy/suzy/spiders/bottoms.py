import scrapy
from scrapy.linkextractors import LinkExtractor
from suzy.items import BottomsItem, WebExclusivesItem
from scrapy.spiders import CrawlSpider, Rule
import itertools
import json
import re
# from datetime import datetime

class BottomsSpider(scrapy.Spider):
    name = "bottoms"
    allowed_domains = ['www.suzyshier.com']
    rules = [
        Rule(LinkExtractor(allow='products'), callback='parse_item')
    ]

    def start_requests(self):
        urls = [
            'https://suzyshier.com/collections/sz_bottoms_shop-all-bottoms?page=1',
            'https://suzyshier.com/collections/sz_bottoms_shop-all-bottoms?page=2',
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

        # '//*[@id="product-1"]/div/a'
        # '//*[@id="product-4"]/div/div[1]/a'

    def parse(self, response):
        for url in response.xpath('//a/@href').extract():
            if 'products' in url:
                yield scrapy.Request('https://suzyshier.com'+url, callback=self.parse_item)


    def parse_item(self, response):
        item = BottomsItem()
        item['price'] = 0
        return item