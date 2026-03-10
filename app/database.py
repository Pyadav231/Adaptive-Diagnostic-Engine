from pymongo import MongoClient

MONGO_URL = "mongodb://localhost:27017"

client = MongoClient(MONGO_URL)

db = client["adaptive_test"]

questions_collection = db["questions"]
sessions_collection = db["user_sessions"]