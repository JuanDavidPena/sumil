""" Database configuration module """
from pymongo import MongoClient
import os

client = MongoClient(os.getenv("MONGO_URI"))
mydatabase = client.sumil
devs = mydatabase.developers
print(devs)
