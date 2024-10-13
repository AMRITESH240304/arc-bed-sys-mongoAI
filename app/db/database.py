from pymongo import MongoClient
from ..config import settings

collection = None
client = None

def connect_to_mongo():
    global collection, client
    try:
        client = MongoClient(settings.MONGO_URI)
        collection = client['mongoVector']['vectorstore']
        print("Connected to MongoDB")
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")