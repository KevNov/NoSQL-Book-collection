import csv
from pymongo import MongoClient
from pprint import pprint

# Connect to the MongoDB database
client = MongoClient('mongodb://localhost:27017/')
db = client['Homework_nosql']

# insert multiple data to the collection
collection = db['Book collection']
many = [
        {
        "nama": "Outliers: The Story of Success",
        "author": "Malcom Gladwell",
        "tags": "Self-help",
        "harga": 75000,
        "stock": 7
        },
        {
        "nama": "All Hallows",
        "author": "Christopher Goldens",
        "tags": "Horror",
        "harga": 125000,
        "stock": 6
        },
        {
        "nama": "Back in a Spell",
        "author": "Lana Harper",
        "tags": "Romance",
        "harga": 150000,
        "stock": 10
        },
        {
        "nama": "In a Jam",
        "author": "Kate Canterberry",
        "tags": "Humor",
        "harga": 90000,
        "stock": 4
        },
        {
        "nama": "Lesson In Chemistry",
        "author": "Bonnie Garmus",
        "tags": "Historical Fiction",
        "harga": 105000,
        "stock": 9
        }
        ]
for record in many:
    # To ignore the data that already exist
    collection.update_many(record, {'$set': record}, upsert=True)

# Write the data to a CSV file
with open('output/book_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['nama', 'author', 'tags', 'harga', 'stock'])
    for record in collection.find():
        # Print the inserted data
        pprint(record)
        writer.writerow([record['nama'], record['author'], record['tags'], record['harga'], record['stock']])
