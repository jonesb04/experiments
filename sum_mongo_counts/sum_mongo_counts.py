"""
This module contains the functions that will be used to query the mongoDB

Dependencies:
    pymongo
"""
from pymongo import MongoClient


def connect_mongo_db():
    client = MongoClient('localhost', 27017)
    try:
        print(client.server_info())

    except Exception:
        print("Unable to connect to the server.")

    return client


def get_done_counts(db):
    dockets_count = int(db['mirrulations']['dockets'].count_documents({}))
    docs_count = int(db['mirrulations']['documents'].count_documents({}))
    comments_count = int(db['mirrulations']['comments'].count_documents({}))
    return dockets_count + docs_count + comments_count


client = connect_mongo_db()
print(get_done_counts(client))
