# -*- coding: utf-8 -*-
#scrapy crawl example -t csv -o fotocasa.csv --loglevel=INFO
import scrapy
from fotocasa.items import FotocasaItem

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
        item = FotocasaItem()
        item['link'] = response.url
        #TODO extraccion de la información

        yield item