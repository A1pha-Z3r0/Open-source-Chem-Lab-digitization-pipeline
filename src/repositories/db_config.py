"""
This file has a a connection to mongoDB cloud atlas as well as a local client depending on requirements.
Since atlas free tier has only 512mb use local to test and have fun
"""

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv()

pwd = os.getenv("pwd")

def database_config(method = "local"):
    
     # name of the DB
    db_name = "ocr-pipeline"
    collection_name = "All-files"

    if (method == "cloud"):
        uri = f"mongodb+srv://A1phaZ3r0:{pwd}@ocr-pipeline.uqdo1k1.mongodb.net/?retryWrites=true&w=majority&appName=ocr-pipeline"
        try:
            # Create a new client and connect to the server
            client = MongoClient(uri, server_api=ServerApi('1'))
            # Send a ping to confirm a successful connection
            client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)

    else:
        try:
        # Create a new client and connect to the server
            client = MongoClient("mongodb://localhost:27017/")
            # Send a ping to confirm a successful connection
            client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)

    # db and collection creation are idempotent
    db = client[db_name]
    collection = db[collection_name]

    return client, db, collection




