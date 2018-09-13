# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BottomsItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    color = scrapy.Field()
    sizes = scrapy.Field()
    specs = scrapy.Field()
    description = scrapy.Field()

class WebExclusivesItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    discount_price = scrapy.Field()

