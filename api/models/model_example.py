from pymongo import MongoClient as Connection
from bson import ObjectId
from itertools import imap

class Model(dict):
    """
    A simple model that wraps mongodb document
    """
    __getattr__ = dict.get
    __delattr__ = dict.__delitem__
    __setattr__ = dict.__setitem__

    def save(self):
        if not self._id:
            self.collection.insert(self)
        else:
            self.collection.update(
                { "_id": ObjectId(self._id) }, self)

    def reload(self):
        if self._id:
            self.update(self.collection\
                    .find_one({"_id": ObjectId(self._id)}))

    def remove(self):
        if self._id:
            self.collection.remove({"_id": ObjectId(self._id)})
            self.clear()


# ------------------------------
# Here is the example model
# ------------------------------

class Document(Model):
    collection = Connection()["test_db"]["test_collection"]

    @property
    def keywords(self):
        return self.title.split()

# ------------------------------
# Creating new document
# ------------------------------

document = Document({
    "title": "test document",
    "slug": "test-document"
})

print(document._id)# none
document.save()
print(document._id) # "50d3cb0068c0064a21e76be4"

# -------------------------
# Getting a single document
# -------------------------

document2 = Document({
    "_id": document._id
})

print(document2.title) # None
document.reload()
print(document2.title) # "test document"

# -----------------
# Updating document
# -----------------

document.title = "test document 2"
document.save()
print(document.title) # "test document 2"
document.reload()
print(document.title) # "test document 2"

# -----------------
# Removing document
# -----------------

document.remove()
print(document) # {}

# ------------------------------
# Mapping documents to the model
# ------------------------------

documents = imap(Document, Document.collection.find())

# that's all

for document in documents:
    print(document.title, document.keywords)
