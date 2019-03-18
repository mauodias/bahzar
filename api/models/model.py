from bson import ObjectId

class Model(dict):
  __getattr__ = dict.get
  __delattr__ = dict.__delitem__
  __setattr__ = dict.__setitem__

  def save(self):
    if not self._id:
      self.collection.insert(self)
    else:
      self.collection.update({"_id": ObjectId(self._id)}, self)

  def reload(self):
    if self._id:
      self.update(self.collection.find_one({"_id": ObjectId(self._id)}))

  def remove(self):
    if self._id:
      self.collection.remove({"_id": ObjectId(self._id)})
      self.clear()

  @classmethod
  def get_items(cls, fields=None):
    results = []
    for item in cls.collection.find(fields if fields else {}):
      results.append(cls.init_with_document(item))
    return results

  @classmethod
  def get_item(cls, _id):
    if not isinstance(_id, ObjectId):
      _id = ObjectId(_id)
    result = cls.collection.find_one({'_id': _id})
    if result:
      return cls.init_with_document(result)
    else:
      return None
