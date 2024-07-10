import os
from dotenv import load_dotenv

from pymongo import MongoClient

load_dotenv()

def get_client():
    try:
        client = MongoClient(os.getenv("MONGO_URI"))
        return client
    except Exception as e:
        raise Exception(f"Error connecting to the database: {e}")

def get_database(client):
    try:
        db = client[os.getenv("MONGODB_DATABASE_NAME")]
        return db
    except Exception as e:
        raise Exception(f"Error connecting to the database: {e}")

def get_collection(db, collection_type):
    try:
        if collection_type == "users":
            collection_name = os.getenv("MONGODB_USERS_COLLECTION_NAME")
        if collection_type == "data":
            collection_name = os.getenv("MONGODB_DATA_COLLECTION_NAME")
        collection = db[collection_name]
        return collection
    except Exception as e:
        raise Exception(f"Error connecting to the database: {e}")