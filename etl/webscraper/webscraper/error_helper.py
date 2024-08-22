
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError, TCPTimedOutError

def handle_spider_error(logger, failure):
    # log all failures
    logger.error(repr(failure))

    # in case you want to do something special for some errors,
    # you may need the failure's type:
    if failure.check(HttpError):
        # these exceptions come from HttpError spider middleware
        # you can get the non-200 response
        response = failure.value.response
        logger.error("HttpError on %s", response.url)

    elif failure.check(DNSLookupError):
        # this is the original request
        request = failure.request
        logger.error("DNSLookupError on %s", request.url)

    elif failure.check(TimeoutError, TCPTimedOutError):
        request = failure.request
        logger.error("TimeoutError on %s", request.url)
