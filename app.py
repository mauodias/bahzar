from flask import Flask, request, Response
import json

import products

app = Flask(__name__)

@app.route('/')
def index():
  return "Bahzar"

@app.route('/create', methods=['POST'])
def createProduct():
  requestData = request.get_json()
  owner = requestData['owner']
  name = requestData['name']
  price = requestData['price']
  description = requestData['description']
  tags = requestData['tags']
  product_id = products.createProduct(owner=owner, name=name, price=price, description=description, tags=tags)
  if product_id:
    product = {"product_id": product_id}
    return Response(json.dumps(product), status=201, mimetype='application/json')
  else:
    error = {"error": product_id}
    return Response(json.dumps(error), status=500, mimetype='application/json')

@app.route('/list')
def listProducts():
  return products.listProducts()
