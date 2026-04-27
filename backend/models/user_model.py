from config import db

collection = db["users"]

def get_users():
    return list(collection.find({}, {"_id": 0}))