import os
from pymongo import MongoClient

MONGODB_URL = os.environ.get('MONGODB_URL', 'mongodb://localhost:27017')

def get_connection():
  return MongoClient(MONGODB_URL)["bahzar"]
