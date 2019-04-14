# -*- coding: utf-8 -*-

import scrapy
from parqueInmobiliario.items import InmuebleItem
from urllib.parse import urlparse

class FotocasaSpider(scrapy.Spider):
    name = 'fotocasa'
    def start_requests(self):
        urls = [
            'https://www.fotocasa.es/es/comprar/viviendas/madrid-provincia/madrid-zona-de/l',
            #'https://www.fotocasa.es/es/comprar/viviendas/madrid-provincia/madrid-zona-de/l?sortType=publicationDate&latitude=40.415&longitude=-3.71036&combinedLocationIds=724,14,28,173,0,0,0,0,0&gridType=3',
            #'https://www.fotocasa.es/es/comprar/viviendas/madrid-provincia/madrid-zona-de/l/2?sortType=publicationDate&amp;latitude=40.415&amp;longitude=-3.71036&amp;combinedLocationIds=724,14,28,173,0,0,0,0,0&amp;gridType=3'

        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
#App > div > div.re-Page > div > div.re-Searchpage-wrapper > div.re-Searchresult-wrapper > div.re-Searchresult > div:nth-child(2) > div > div > div.sui-CardComposable-primary > div > a
    def parse(self, response):

        for i in range(1,20):
            link = "https://www.fotocasa.es/es/comprar/viviendas/madrid-provincia/madrid-zona-de/l/" + str(i)
            yield scrapy.Request(link, self.parse_pagina)
        
    def parse_pagina(self, response):
        links = response.xpath('//a[@class="re-CardImage-link"]/@href').extract()
        precios = response.xpath('//span[@class="re-Card-price"]/text()').extract()
        #habitaciones = response.xpath('//span[@class="re-Card-wrapperFeatures"]/span/text()')[0].extract()
        #superficies = response.xpath('//span[@class="re-Card-wrapperFeatures"]/span/text()')[1].extract()
        print(links)
        for i in range(0,len(links)):
            item = InmuebleItem()
            item['precio'] = precios[i]
            item ['link'] = 'https://www.fotocasa.es' + links[i]
            request = scrapy.Request(item['link'], callback=self.parse_vivienda, meta={'item': item})
            yield request

    def parse_vivienda(self, response):
                
        item = InmuebleItem()
        item['ciudad'] = response.xpath( '//a[@class = "re-Breadcrumb-link"]/text()' )[2].get()
        #item['codigoPostal'] = response.xpath( '//p[@class = "fc-DetailDescription"]/text()' ).re_first( r'[0-9]{5}' )
        item['comunidad'] = response.xpath( '//a[@class = "re-Breadcrumb-link"]/text()' )[0].get()
        item['habitaciones'] = response.xpath( '//li[@class = "re-DetailHeader-featuresItem"]/text()' )[0].re_first( r"[0-9]+ hab" )
        item['banos'] = response.xpath( '//li[@class = "re-DetailHeader-featuresItem"]/text()' )[1].re_first( r'[0-9]+ baño' )       
        item['superficie'] = response.xpath( '//li[@class = "re-DetailHeader-featuresItem"]/text()' )[2].re_first( r'[0-9]+' )
        item['planta'] = response.xpath( '//li[@class = "re-DetailHeader-featuresItem"]/text()' )[3].re_first( r'[0-9]+' )
        item['precio'] = response.xpath( '//span[@class = "re-DetailHeader-price"]/text()' ).re_first( r'[0-9]+\.[0-9]+' )
        item['referencia'] = response.xpath( '//span[@class = "re-DetailReference"]/text()' ).re_first( r'[0-9]+' )
        item['particular'] = 'Profesional' if response.xpath( '//div[@class = "re-ContactDetail-inmo"]' ) else 'Particular'
        item['web'] = 'Fotocasa'
        item['link'] = response.url
        

        yield item
