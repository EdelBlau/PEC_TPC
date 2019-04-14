# -*- coding: utf-8 -*-
import scrapy
from parqueInmobiliario.items import InmuebleItem

class PisosSpider(scrapy.Spider):
    name = 'pisos'
    def start_requests(self):
        urls = [
            'https://www.pisos.com/venta/pisos-madrid/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for i in range(1,20):
            link = "https://www.pisos.com/venta/pisos-madrid/" + str(i) + '/'
            yield scrapy.Request(link, self.parse_pagina)

    def parse_pagina(self, response):
        links = response.xpath('//meta[@itemprop="url"]/@content').extract()
        for link in links:
            request = scrapy.Request('https://www.pisos.com' + link, callback=self.parse_vivienda)
            yield request


    def parse_vivienda(self, response):
        item = InmuebleItem()
        item['precio'] = response.xpath( '//div[@class = "priceBox-price"]/span/text()' ).get()
        item['superficie'] = response.xpath( '//div[@class = "basicdata-item"]/text()' )[0].re_first(r'[0-9]+')
        item['habitaciones'] = response.xpath( '//div[@class = "basicdata-item"]/text()' )[1].re_first( r"[0-9]+" )
        item['banos'] = response.xpath( '//div[@class = "basicdata-item"]/text()' )[2].re_first( r'[0-9]+' )
        item['referencia'] = response.xpath('//li[@class="charblock-element more-padding"]//text()').re(r':(.*-.*)')
        item['particular'] = 'Profesional' if response.xpath( '//div[@class = "owner-data-logo"]' ) else 'Particular'
        item['ciudad'] = response.xpath( '//h2[@class = "position"]/text()' ).extract_first()
        item['comunidad'] = response.xpath( '//h2[@class = "position"]/text()' ).extract_first()
        
        '''        
        #item['codigoPostal'] = response.xpath( '//p[@class = "fc-DetailDescription"]/text()' ).re_first( r'[0-9]{5}' )
        item['planta'] = response.xpath( '//li[@class = "re-DetailHeader-featuresItem"]/text()' )[3].re_first( r'[0-9]+' )
        '''
        item['web'] = 'Pisos'
        item['link'] = response.url

        yield item
