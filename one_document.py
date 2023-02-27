import csv
from pymongo import MongoClient
from pprint import pprint

# Connect to the MongoDB database
client = MongoClient('mongodb://localhost:27017/')
db = client['Homework_nosql']

# insert one data to the collection
collection = db['Book collection']
data = [
        {
        "nama" : "12 Rules For Life", 
        "author" : "Jordan B.Petterson", 
        "tags" : "Self Improvements", 
        "harga" : 175000, 
        "stock" : 12
        }
        ]

for record in data:
    # to Ignore the data that already exist
    collection.update_one(record, {'$set': record}, upsert=True)

# Write the data to a CSV file
with open('output/book_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['nama', 'author', 'tags', 'harga', 'stock'])
    for record in collection.find():
        # Print the inserted data
        pprint(record)
        writer.writerow([record['nama'], record['author'], record['tags'], record['harga'], record['stock']])