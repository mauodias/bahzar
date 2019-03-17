from .db import get_connection
from .model import Model

class Product(Model):
  collection = get_connection()['products']  

  def __init__(self, owner, name, price, description, _id=None, available=True, images=[]):
    self._id = _id
    self.owner = owner
    self.name = name
    self.price = price
    self.description = description
    self.available = available
    self.images = images

  def sell(self):
    self.available = False
    return True

  def insert_images(self, images):
    for image in images:
      self.images.append(image)

  @classmethod
  def init_with_document(cls, document):
    _id = document.get('_id', None)
    owner = document.get('owner', None)
    name = document.get('name', None)
    price = document.get('price', None)
    description = document.get('description', None)
    available = document.get('available', None)
    images = document.get('images', None)
    return cls(_id=_id, owner=owner, name=name, price=price, description=description, available=available, images=images)

  @classmethod
  def get_products(cls, owner=None):
    results = []
    for product in cls.collection.find({'owner': owner} if owner else {}):
      results.append(cls.init_with_document(product))
    return results

  @classmethod
  def get_product(cls, _id):
    result = cls.collection.find_one({'_id': _id})
    if result:
      return cls.init_with_document(result)
    else:
      return None
