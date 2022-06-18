""" Database configuration module """
from pymongo import MongoClient

client = MongoClient("mongodb+srv://sumil:sumilhackaton2022@cluster0.pzkkgt4.mongodb.net/?retryWrites=true&w=majority")
mydatabase = client.sumil
devs = mydatabase.developers
print(devs)
