import uuid
from scrapy.crawler import CrawlerRunner, CrawlerProcess
from twisted.internet import reactor
from webscraper.spiders.webpage_spider import WebpageCrawler
from scrapy.utils.project import get_project_settings

url = "https://docs.scrapy.org/en/latest/intro/tutorial.html"
run_id = str(uuid.uuid4())

settings = get_project_settings()
use_crawler = False
if use_crawler:
    print("using crawler process")
    process = CrawlerProcess(settings)
    process.crawl(WebpageCrawler, url=url, run_id=run_id)
    process.start()
else:
    print("using crawler runner")
    runner = CrawlerRunner(settings)
    d = runner.crawl(WebpageCrawler, url=url, run_id=run_id)
    d.addBoth(lambda _: reactor.stop())
    reactor.run()

