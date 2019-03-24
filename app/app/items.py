# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class KitamuraUsedItem(scrapy.Item):
    # define the fields for your item here like:
    ac = scrapy.Field()
    maker = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    shop = scrapy.Field()
    state = scrapy.Field()
    date = scrapy.Field()

class MapcameraUsedItem(scrapy.Item):

    mapcode = scrapy.Field()
    jancode = scrapy.Field()
    name = scrapy.Field()
    maker = scrapy.Field()
    price = scrapy.Field()
    state = scrapy.Field()
    point = scrapy.Field()
    # pass