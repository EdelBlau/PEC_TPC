# -*- coding: utf-8 -*-
import scrapy
from parqueInmobiliario.items import InmuebleItem

class PisosSpider(scrapy.Spider):
    name = 'pisos'

    def __init__(self, *args, **kwargs):

        super(PisosSpider, self).__init__(*args, **kwargs)
        self.start_urls = [
            "https://www.pisos.com/venta/pisos-"+ kwargs.get('ciudad') +"/"
        ]

    def parse(self, response):
        for i in range(1,20):
            link = response.url + str(i) + '/'
            yield scrapy.Request(link, self.parse_pagina)

    def parse_pagina(self, response):
        links = response.xpath('//meta[@itemprop="url"]/@content').extract()
        for link in links:
            request = scrapy.Request('https://www.pisos.com' + link, callback=self.parse_vivienda)
            yield request


    def parse_vivienda(self, response):
        item = InmuebleItem()
        item['precio'] = response.xpath( '//div[@class = "priceBox-price"]/span/text()' ).re_first(r'(.*)€')
        item['superficie'] = response.xpath( '//div[@class = "basicdata-item"]/text()' )[0].re_first(r'[0-9]+')
        item['habitaciones'] = response.xpath( '//div[@class = "basicdata-item"]/text()' )[1].re_first( r"[0-9]+" )
        item['banos'] = response.xpath( '//div[@class = "basicdata-item"]/text()' )[2].re_first( r'[0-9]+' )
        item['referencia'] = response.xpath('//li[@class="charblock-element more-padding"]//text()').re(r':(.*-.*)')
        item['particular'] = 'Profesional' if response.xpath( '//div[@class = "owner-data-logo"]' ) else 'Particular'
        item['ciudad'] = response.xpath( '//h2[@class = "position"]/text()' ).re_first(r'\((.*)\)') or response.xpath( '//h2[@class = "position"]/text()' ).extract_first()
        item['comunidad'] = response.xpath( '//div[@class = "footer-breadcrumb"]/div[@class="item"][2]/a/text()' ).extract_first()
    
        item['web'] = 'Pisos'
        item['link'] = response.url

        yield item
