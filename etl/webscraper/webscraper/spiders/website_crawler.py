from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from webscraper.items import WebscraperItem

class WebsiteCrawler(CrawlSpider):
    name = "website_crawler"

    rules = (Rule(LinkExtractor(allow="*"), callback="parse_item"))

    def parse_item(self, response):
        item = WebscraperItem()
        item['text'] = response.text
        item['url'] = response.url
        return item
