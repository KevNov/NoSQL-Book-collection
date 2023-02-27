import csv
from pymongo import MongoClient
from pprint import pprint

# Connect to the MongoDB database
client = MongoClient('mongodb://localhost:27017/')
db = client['Homework_nosql']

# Connect to MongoDB collection
collection = db['Book collection']

# Update multiple data 
updates = [
    {
        'filter': {'nama': 'Outliers: The Story of Success'},
        'update': {'$set': {'harga': 85000, 'stock': 11}}
    },
    {
        'filter': {'nama': 'All Hallows'},
        'update': {'$set': {'harga': 140000, 'stock': 1}}
    },
    {
        'filter': {'nama': 'Back in a Spell'},
        'update': {'$set': {'harga': 125000, 'stock': 24}}
    },
    {
        'filter': {'nama': 'In a Jam'},
        'update': {'$set': {'harga': 120000, 'stock': 35}}
    },
    {
        'filter': {'nama': 'Lesson In Chemistry'},
        'update': {'$set': {'harga': 119000, 'stock': 4}}
    },
]

# Update the documents
for update in updates:
    collection.update_many(update['filter'], update['update'], upsert=True)

# Write the data to a CSV file
with open('output/data_update.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['nama', 'author', 'tags', 'harga', 'stock'])
    for record in collection.find():
        # Print the updated data
        pprint(record)
        writer.writerow([record['nama'], record['author'], record['tags'], record['harga'], record['stock']])

