from datetime import datetime
import pymongo
import config

client = pymongo.MongoClient(f"mongodb://{config.login}:{config.password}@{config.host}/{config.db_name}")
db = client["jokes_db"]
collection = db["jokes"]
if collection.estimated_document_count() == 0:
    collection.drop()
    collection.create_index([("tag", pymongo.ASCENDING), ("date", pymongo.ASCENDING)])


def filling_data(tag, new_joke_list):
    date = datetime.now()
    data = ""
    for element in new_joke_list:
        joke = {
            "tag": tag[0],
            "data": data,
            "content": element,
            "date": date
        }
        collection.insert_one(joke)
