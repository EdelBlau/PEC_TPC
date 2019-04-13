# -*- coding: utf-8 -*-
#scrapy crawl example -t csv -o fotocasa.csv --loglevel=INFO
import scrapy
from fotocasa.items import FotocasaItem
from urllib.parse import urlparse

class ExampleSpider(scrapy.Spider):
    name = 'example'
    def start_requests(self):
        urls = [
            'https://www.fotocasa.es/es/comprar/viviendas/madrid-provincia/madrid-zona-de/l?sortType=publicationDate&latitude=40.415&longitude=-3.71036&combinedLocationIds=724,14,28,173,0,0,0,0,0&gridType=3',
            'https://www.fotocasa.es/es/comprar/viviendas/madrid-provincia/madrid-zona-de/l/2?sortType=publicationDate&amp;latitude=40.415&amp;longitude=-3.71036&amp;combinedLocationIds=724,14,28,173,0,0,0,0,0&amp;gridType=3'

        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
#App > div > div.re-Page > div > div.re-Searchpage-wrapper > div.re-Searchresult-wrapper > div.re-Searchresult > div:nth-child(2) > div > div > div.sui-CardComposable-primary > div > a
    def parse(self, response):
        links = response.xpath('//a[@class="re-CardImage-link"]/@href').extract()
        for link in links:
            request = scrapy.Request('https://www.fotocasa.es/es' + link, callback=self.parse_vivienda)
            yield request

    def parse_vivienda(self, response):
        parsed_uri = urlparse( response.url )
        
        item = FotocasaItem()
        item['banos'] = response.xpath( '//li[@class = "re-DetailHeader-featuresItem"]/text()' )[1].re_first( r'[0-9]+' )
        #TODO item['caracteristicas'] =
        item['ciudad'] = response.xpath( '//a[@class = "re-Breadcrumb-link"]/text()' )[3].get()
        item['codigoPostal'] = response.xpath( '//p[@class = "fc-DetailDescription"]/text()' ).re_first( r'[0-9]{5}' )
        item['comunidad'] = response.xpath( '//a[@class = "re-Breadcrumb-link"]/text()' )[0].get()
        item['habitaciones'] = response.xpath( '//li[@class = "re-DetailHeader-featuresItem"]/text()' )[0].re_first( r'[0-9]+' )
        item['link'] = response.request.url
        #TODO item['localidad'] =
        item['particular'] = 'Profesional' if response.xpath( '//div[@class = "re-ContactDetail-inmo"]' ) else 'Particular'
        item['planta'] = response.xpath( '//li[@class = "re-DetailHeader-featuresItem"]/text()' )[3].re_first( r'[0-9]+' )
        item['precio'] = response.xpath( '//span[@class = "re-DetailHeader-price"]/text()' ).re_first( r'[0-9]+\.[0-9]+' )
        item['precio_m'] = response.xpath( '//li[@class = "re-DetailHeader-featuresItem"]/text()' )[4].re_first( r'[0-9]+\.[0-9]+' )
        item['referencia'] = response.xpath( '//span[@class = "re-DetailReference"]/text()' ).re_first( r'[0-9]+' )
        item['superficie'] = response.xpath( '//li[@class = "re-DetailHeader-featuresItem"]/text()' )[2].re_first( r'[0-9]+' )
        item['web'] = '{uri.netloc}'.format( uri = parsed_uri )

        yield item
