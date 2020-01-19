# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FlipkartItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    brand = scrapy.Field()
    price = scrapy.Field()
    seller = scrapy.Field()
    image1 = scrapy.Field()
    image2 = scrapy.Field()
    image3 = scrapy.Field()
    image4 = scrapy.Field()

    pass
