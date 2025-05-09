# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from infra.mongodb_connector import MongoDBConnector

class MongoDBPipeline:
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get("MONGO_URI"),
            mongo_db=crawler.settings.get("MONGO_DB", "scrapy_db")
        )

    def open_spider(self, spider):
        self.connector = MongoDBConnector(self.mongo_uri, self.mongo_db)

    def close_spider(self, spider):
        self.connector.close()

    def process_item(self, item, spider):
        self.connector.save_item("json_data", dict(item))
        return item
