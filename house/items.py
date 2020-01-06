# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HouseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    name = scrapy.Field()
    labels = scrapy.Field()

    area = scrapy.Field()
    region = scrapy.Field()
    street = scrapy.Field()
    capacity = scrapy.Field()
    room_type = scrapy.Field()
    house_type = scrapy.Field()

    price = scrapy.Field()
    mean_price = scrapy.Field()
    time = scrapy.Field()

