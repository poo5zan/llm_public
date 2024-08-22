from scrapy import Spider, Request
from scrapy.http import TextResponse
from webscraper.items import WebscraperItem
from webscraper.error_helper import handle_spider_error
from webscraper.time_helper import TimeHelper

class WebpageCrawler(Spider):
    name = "webpage_spider"
    def __init__(self, url: str = None):
        super().__init__()
        self.url = "https://docs.scrapy.org/en/latest/intro/tutorial.html"
        self.time_helper = TimeHelper()

    def start_requests(self):
        yield Request(url = self.url,
                      callback=self.parse,
                      errback=self.errback)

    def parse(self, response: TextResponse):
        item = WebscraperItem()
        item['url'] = response.url
        item['created_date'] = str(self.time_helper.get_utc_now())
        item['text'] = response.text
        return item
    
    def errback(self, failure):
        handle_spider_error(self.logger, failure)
