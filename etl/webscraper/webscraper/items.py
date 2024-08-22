# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field

class WebscraperItem(Item):
    # define the fields for your item here like:
    text = Field()
    url = Field()
    created_date = Field()
