import scrapy
from suzy.items import BottomsItem, WebExclusivesItem


class BottomsSpider(scrapy.Spider):
    name = "bottoms"
    allowed_domains = ['suzyshier.com']

    def start_requests(self):
        urls = [
            'https://suzyshier.com/collections/sz_bottoms_shop-all-bottoms?page=1',
            'https://suzyshier.com/collections/sz_bottoms_shop-all-bottoms?page=2',
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for url in response.xpath('//a/@href').extract():
            if 'products' in url and 'http' in url:
                yield scrapy.Request(url, callback=self.parse_item)
            elif 'products' in url:
                yield scrapy.Request('https://suzyshier.com' + url, callback=self.parse_item)

    def parse_item(self, response):
        item = BottomsItem()
        item['title'] = response.xpath('//h1[contains(@class,"product__header")]/text()').extract_first()
        item['price'] = response.xpath('//span[contains(@class,"product__price")]/text()').extract_first().strip()
        item['color'] = response.xpath('//label[contains(@class,"radio-color")]/@data-value').extract()
        item['sizes'] = response.xpath('//label[contains(@class,"radio-size")]/@data-value').extract()
        item['specs'] = response.xpath('//*[@id="toggle-product__specs"]/ul/li/text()').extract()
        item['description'] = response.xpath('//*[@id="toggle-product__description"]/text()').extract_first().strip()
        yield item


class WebExclusivesSpider(scrapy.Spider):
    name = "exclusives"
    allowed_domains = ['suzyshier.com']

    def start_requests(self):
        urls = [
            'https://suzyshier.com/collections/sz_trend_online-exclusives?page=1',
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for url in response.xpath('//a/@href').extract():
            if 'products' in url and 'http' in url:
                yield scrapy.Request(url, callback=self.parse_item)
            elif 'products' in url:
                yield scrapy.Request('https://suzyshier.com' + url, callback=self.parse_item)

    def parse_item(self, response):
        item = WebExclusivesItem()
        item['title'] = response.xpath('//h1[contains(@class,"product__header")]/text()').extract_first()
        item['price'] = response.xpath('//span[contains(@class,"product__price")]/text()').extract_first().strip()
        item['discount_price'] = response.xpath('//span[contains(@class,"product__discount")]/text()').extract_first()
        if item['discount_price']:
            item['discount_price'] = item['discount_price'].strip()
        yield item
