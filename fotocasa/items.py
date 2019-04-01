# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class FotocasaItem(scrapy.Item):
    referencia = Field()
    nombre = Field()
    precio = Field()
    particular = Field()
    imagenes = Field()
    habitaciones = Field()
    banos = Field()
    superficie = Field()
    planta = Field()
    precio_m = Field()
    caracteristicas = Field()
    link = Field()
    web = Field()
    ciudad = Field()
    comunidad = Field()
    codigoPostal = Field()
    localidad = Field()
    telefono = Field()
