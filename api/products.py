import json
from bson.json_util import dumps
from tools import get_connection

def createProduct(owner, name, price, description, tags):
  connection = db.get_connection()
  products = connection['products']
  product = {
    'owner': owner,
    'name': name,
    'price': price,
    'description': description,
    'tags': tags,
    'status': 'available'
  }
  product_id = products.insert_one(product)
  return str(product_id.inserted_id)

def listProducts():
  connection = get_connection()
  products = connection['products']
  return dumps(list(products.find()))
