"""
This module contains the functions that will be used to query the mongoDB

Dependencies:
    pymongo
"""
import pymongo
import os
from pymongo import MongoClient

client = MongoClient('localhost', 27017)

try:
    print(client.server_info())

except Exception:
    print("Unable to connect to the server.")

db = client.mirrulations
print(db.list_collection_names())