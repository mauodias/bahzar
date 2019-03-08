from .db import get_connection
from .model import Model

class Product(Model):
  collection = get_connection()['products']  

  def __init__(self, owner, name, price, description):
    self.owner = owner
    self.name = name
    self.price = price
    self.description = description
    self.available = True
    self.images = []

  def sell(self):
    self.available = False
    return True

  def insert_images(self, images):
    for image in images:
      self.images.append(image)
