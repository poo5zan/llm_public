from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from webscraper.domain_helper import DomainHelper
from webscraper.items import WebscraperItem
from webscraper.error_helper import handle_spider_error
from webscraper.time_helper import TimeHelper

class WebsiteCrawler(CrawlSpider):
    name = "website_crawler_spider"
    rules = [
        Rule(LinkExtractor(allow=r'.*'),
             callback="parse_item",
             errback="errback",
             follow=True)]
    
    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)
        self.url = kw.get("url", "")
        if self.url == "":
            raise ValueError("URL is required to scrape")
        self.start_urls = [self.url]
        self.allowed_domains = [DomainHelper().extract_domain_from_url(self.url)]
        self.run_id = kw.get("run_id", "")
        if self.run_id == "":
            raise ValueError("run_id is required")

        self.time_helper = TimeHelper()

    def parse_item(self, response):
        item = WebscraperItem()
        item['url'] = response.url
        item['created_date'] = str(self.time_helper.get_utc_now())
        item['text'] = response.text
        return item
    
    def errback(self, failure):
        handle_spider_error(self.logger, failure)
