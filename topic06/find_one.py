from bson.objectid import ObjectId

from pymongo import MongoClient
from pymongo.server_api import ServerApi
from credentials import mongo_host

client = MongoClient(
    mongo_host,
    server_api=ServerApi('1')
)

db = client.book

result = db.cats.find_one({"_id": ObjectId("60d24b783733b1ae668d4a77")})
print(result)
