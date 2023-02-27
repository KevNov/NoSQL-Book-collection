import csv
from pymongo import MongoClient
from pprint import pprint

# Connect to the MongoDB database
client = MongoClient('mongodb://localhost:27017/')
db = client['Homework_nosql']

# Connect to MongoDB collection
collection = db['Book collection']

# Update the "harga" and "stock" field in the document
query = {"nama": "In a Jam"}
new_values = {"$set": {"harga": 140000,"stock" : 25}}
collection.update_one(query, new_values)

# Write the data to a CSV file
with open('output/book_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['nama', 'author', 'tags', 'harga', 'stock'])
    for record in collection.find():
        # Print the updated data
        pprint(record)
        writer.writerow([record['nama'], record['author'], record['tags'], record['harga'], record['stock']])