import os
import datetime
import pymongo
from pymongo import MongoClient
 
MONGO_URL = 'mongodb://tornado:pT3mW49P81u@widmore.mongohq.com:10010/Dubsit'
client = MongoClient(MONGO_URL)

db = client.Dubsit
collection = db.relevance

def GIF(URL, up, down):
	gifDB = collection.find_one({"url": URL})
	if up is True:
		gifDB['score'] += 1
	if down is True:
		gifDB['score'] += 0.5
	collection.save(gifDB)