from typing import Any
from scrapy.http import Response, response
import scrapy



class OzonSpider(scrapy.Spider):
    name = 'ozon'
    start_urls = ['https://www.ozon.ru/category/smartfony-15502/?sorting=rating']

    def parse(self, response: Response, **kwargs: Any) -> Any:
        for link in response.css('a.tile-hover-target'):
            yield response.follow(link, callback=self.parse_ozon)

        for i in range(1, 5):
            next_page = f'https://www.ozon.ru/category/smartfony-15502/?page={i}&sorting=rating'
            yield response.follow(next_page, callback=self.parse)

    def parse_ozon(self, response):
        yield {
            'OS': response.css('dd.m0k::text'),
        }
