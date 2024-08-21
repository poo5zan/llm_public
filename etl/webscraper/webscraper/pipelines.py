# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter

from storage_service.storage_provider import StorageProvider
from storage_service.storage_provider_factory import StorageProviderFactory

class WebscraperPipeline:
    """
        https://docs.scrapy.org/en/latest/topics/item-pipeline.html

        Typical uses of item pipelines are:
            Cleaning HTML data
            validating scraped data (checking that the items contain certain fields)
            checking for duplicates (and dropping them)
            storing the scraped item in a database
    """

    def process_item(self, item, spider):
        print('in process pipeline ', item.get('url'))
        # store data, call storage service
        # save data to file

        sto = StorageProviderFactory(StorageProvider.FILE_STORAGE)

        return item
