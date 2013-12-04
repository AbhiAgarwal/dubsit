import os
import datetime
import pymongo
from pymongo import MongoClient
 
MONGO_URL = 'mongodb://tornado:pT3mW49P81u@widmore.mongohq.com:10010/Dubsit'
client = MongoClient(MONGO_URL)

db = client.Dubsit
collection = db.timeout

def averageTimeGIF(average, iterations):
	GIFRankHandler = collection.find_one({"name": "GIFRankHandler"})
	GIFRankHandler['avg'] = average
	GIFRankHandler['iter'] = iterations
	collection.save(GIFRankHandler)

def averageTimeNews(average, iterations):
	NEWSRankHandler = collection.find_one({"name": "NEWSRankHandler"})
	NEWSRankHandler['avg'] = average
	NEWSRankHandler['iter'] = iterations
	collection.save(NEWSRankHandler)

def getGIF():
	GIFRankHandler = collection.find_one({"name": "GIFRankHandler"})
	return {'avg': GIFRankHandler['avg'], 'iter': GIFRankHandler['iter']}

def getNews():
	NEWSRankHandler = collection.find_one({"name": "NEWSRankHandler"})
	return {'avg': NEWSRankHandler['avg'], 'iter': NEWSRankHandler['iter']}