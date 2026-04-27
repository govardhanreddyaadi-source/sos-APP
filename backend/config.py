from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:1234@sosemergency.iy3mloj.mongodb.net/?appName=sosemergency")
db = client["sos_emergency"]
