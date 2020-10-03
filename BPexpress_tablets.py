# -*- coding: utf-8 -*-
import scrapy


class AliexpressTabletsSpider(scrapy.Spider):
    name = 'aliexpress_tablets'
    allowed_domains = ['https://www.bureauxapartager.com/location-bureau-paris']
    start_urls = ['https://www.bureauxapartager.com/location-bureau-paris/']

    def parse(self, response):

        #Extracting the content using css selectors
        offer__details = response.css('.offer__details::text').extract()
        offer__surface = response.css('.offer__surface::text').extract()
        offer__capacity = response.css('.offer__capacity::text').extract()
        #offer_title__link = response.css('.offer-title__link::text').extract()
        #price_selector = selector.xpath('.//*[@itemscope]')


        #Give the extracted content row wise
        for item in zip(offer__details,offer__surface,offer__capacity): #,offer_title__link
            #create a dictionary to store the scraped info
            scraped_info = {
                'offer__details' : item[0],
                'offer__surface' : item[1],
                'offer__capacity' : item[2],
                #'offer_title__link' : item[3],
            }

            #yield or give the scraped info to scrapy
            yield scraped_info
            
            
#EspaceBureau = response.xpath('//span[@class=$value]/span/text()', value='offer__details').extract()            