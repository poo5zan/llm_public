from scrapy import Spider, Request
from scrapy.http import TextResponse
from webscraper.items import WebscraperItem

class WebpageCrawler(Spider):
    name = "webpage_spider"
    def __init__(self, url: str = None):
        super().__init__()
        self.url = "https://docs.scrapy.org/en/latest/intro/tutorial.html"

    def start_requests(self):
        yield Request(url = self.url, callback=self.parse)

    def parse(self, response: TextResponse):
        item = WebscraperItem()
        item['text'] = response.text
        item['url'] = response.url
        return item
