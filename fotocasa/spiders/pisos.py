# -*- coding: utf-8 -*-
import scrapy
from fotocasa.items import FotocasaItem

class PisosSpider(scrapy.Spider):
    name = 'pisos'
    def start_requests(self):
        urls = [
            'https://www.pisos.com/venta/pisos-madrid/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        links = response.xpath('//meta[@itemprop="url"]/@content').extract()
        for link in links:
            request = scrapy.Request('https://www.pisos.com' + link, callback=self.parse_vivienda)
            yield request

    def parse_vivienda(self, response):
        item = FotocasaItem()
        item['link'] = response.url
        #TODO extraccion de la información

        yield item
