from .db import get_connection
from .model import Model

class User(Model):
  collection = get_connection()['users']

  def __init__(self, email):
    self.email = email

  @staticmethod
  def init_with_document(document):
    _id = document.get('_id', None)
    email = document.get('email', None)
    result = User(email=email)
    result._id = _id
    return result
