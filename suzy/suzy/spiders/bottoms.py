import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://suzyshier.com/collections/sz_bottoms_shop-all-bottoms?page=1',
            'https://suzyshier.com/collections/sz_bottoms_shop-all-bottoms?page=2',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

