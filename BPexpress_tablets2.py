# -*- coding: utf-8 -*-
import scrapy


class AliexpressTablets2Spider(scrapy.Spider):
    name = 'aliexpress_tablets2'
    allowed_domains = ['https://www.bureauxapartager.com/location-bureau-paris']
    start_urls = ['http://https://www.bureauxapartager.com/location-bureau-paris/']

    def parse(self, response):
        pass
