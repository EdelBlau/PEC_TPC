# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class InmuebleItem(scrapy.Item):
    referencia = Field()
    precio = Field()
    particular = Field()
    habitaciones = Field()
    banos = Field()
    superficie = Field()
    link = Field()
    web = Field()
    ciudad = Field()
    comunidad = Field()
    
    

