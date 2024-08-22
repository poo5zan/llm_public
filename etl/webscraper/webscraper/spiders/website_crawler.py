# from scrapy.spiders import CrawlSpider, Rule
# from scrapy.linkextractors import LinkExtractor
# from webscraper.items import WebscraperItem
# from webscraper.error_helper import handle_spider_error

# class WebsiteCrawler(CrawlSpider):
#     pass
#     # name = "website_crawler"

#     # rules = (Rule(LinkExtractor(allow="*"), callback="parse_item", errback="errback"))

#     # def parse_item(self, response):
#     #     item = WebscraperItem()
#     #     item['text'] = response.text
#     #     item['url'] = response.url
#     #     return item
    
#     # def errback(self, failure):
#     #     handle_spider_error(self.logger, failure)
