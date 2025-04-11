import pymongo

class MongoDBConnector:
    def __init__(self, uri, db_name):
        self.client = pymongo.MongoClient(uri)
        self.db = self.client[db_name]

    def save_item(self, collection, item):
        self.db[collection].insert_one(item)

    def get_items(self, collection):
        return list(self.db[collection].find())

    def close(self):
        self.client.close()