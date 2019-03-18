from .db import get_connection
from .model import Model
from bson import ObjectId

class Product(Model):
  collection = get_connection()['products']  

  def __init__(self, owner, name, price, tags, description, available=True, images=[]):
    self.owner = owner
    self.name = name
    self.price = price
    self.tags = tags
    self.description = description
    self.available = available
    self.images = images

  def sell(self):
    self.available = False

  def insert_images(self, images):
    for image in images:
      self.images.append(image)

  @staticmethod
  def init_with_document(document):
    _id = document.get('_id', None)
    owner = document.get('owner', None)
    name = document.get('name', None)
    price = document.get('price', None)
    tags = document.get('tags', None)
    description = document.get('description', None)
    available = document.get('available', True)
    images = document.get('images', [])
    result = Product(owner=owner, name=name, price=price, tags=tags, description=description, available=available, images=images)
    result._id = _id
    return result 
