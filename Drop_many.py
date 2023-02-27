import csv
from pymongo import MongoClient
from pprint import pprint

# Connect to the MongoDB database
client = MongoClient('mongodb://localhost:27017/')
db = client['Homework_nosql']

# Connect to MongoDB collection
collection = db['Book collection']

# Delete multiple documents with a specific coditions
query = {'harga': {'$lt': 100000}}
result = collection.delete_many(query)

# Print the deleted data
pprint(f'{result.deleted_count} document(s) deleted')
