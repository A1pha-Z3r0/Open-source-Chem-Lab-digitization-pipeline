from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv()

pwd = os.getenv("pwd")

uri = f"mongodb+srv://A1phaZ3r0:{pwd}@ocr-pipeline.uqdo1k1.mongodb.net/?retryWrites=true&w=majority&appName=ocr-pipeline"

try:
    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))
    # Send a ping to confirm a successful connection
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# name of the DB
db_name = "ocr-pipeline"

if db_name in client.list_database_names():
    print("Database already exists")
else:
    # create DB
    db = client["ocr-pipeline"]




