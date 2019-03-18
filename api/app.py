from flask import Flask, request, Response
import json
from bson.json_util import default, object_hook

from models import Product, User

app = Flask(__name__)

@app.route('/')
def index():
  return "Bahzar"

@app.route('/createProduct', methods=['POST'])
def createProduct():
  requestData = request.get_json()
  owner = requestData['owner']
  name = requestData['name']
  price = requestData['price']
  description = requestData['description']
  tags = requestData['tags']
  product = Product(owner=owner,name=name, price=price, description=description, tags=tags)
  product.save()
  return Response(json.dumps(product, default=default), status=201, mimetype='application/json')

@app.route('/listProducts', methods=['GET'])
def listProducts():
  return Response(json.dumps(Product.get_items(), default=default), status=201, mimetype='application/json')

@app.route('/createUser', methods=['POST'])
def createUser():
  requestData = request.get_json()
  email = requestData['email']
  user = User(email=email)
  user.save()
  return Response(json.dumps(user, default=default), status=201, mimetype='application/json')

if __name__ == '__main__':
  app.run(host='0.0.0.0')
