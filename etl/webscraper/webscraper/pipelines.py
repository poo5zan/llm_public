# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter

from storage_service.storage_provider import StorageProvider
from storage_service.storage_provider_factory import StorageProviderFactory
from storage_service.storage_service import StorageService

class WebscraperPipeline:
    """
        https://docs.scrapy.org/en/latest/topics/item-pipeline.html

        Typical uses of item pipelines are:
            Cleaning HTML data
            validating scraped data (checking that the items contain certain fields)
            checking for duplicates (and dropping them)
            storing the scraped item in a database
    """

    def open_spider(self, spider):
        storage_provider_factory = StorageProviderFactory(StorageProvider.FILE_STORAGE)
        self.storage_service = StorageService(storage_provider_factory.get_storage_provider_instance())
        
    def process_item(self, item, spider):
        print('in process pipeline ', item.get('url'))
        # store data, call storage service
        # save data to file
        self.storage_service.save()
        
        return item
    