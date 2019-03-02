import os
from pymongo import MongoClient

MONGODB_URL = os.environ['MONGODB_URL']

def get_connection():
  return MongoClient(MONGODB_URL)["bahzar"]
