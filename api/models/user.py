from .db import get_connection
from .model import Model

class User(Model):
  connection = get_connection()['users']

  def __init__(self, email):
    self.email = email
