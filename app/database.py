from pymongo import MongoClient
from app.config import MONGODB_URI, MONGODB_DB

client = MongoClient(MONGODB_URI)
db = client[MONGODB_DB]
events_collection = db.events