import os
import datetime
import pymongo
from pymongo import MongoClient
 
#MONGO_URL = 'mongodb://tornado:pT3mW49P81u@widmore.mongohq.com:10010/Dubsit'
client = MongoClient()

db = client.Dubsit
collection = db.timeout

def averageTimeGIF(average, iterations):
	GIFRankHandler = collection.find_one({"name": "GIFRankHandler"})
	if GIFRankHandler is None:
		GIFRankHandler = {'avg': average, 'iter': iterations}
		collection.insert(GIFRankHandler)
	else:
		GIFRankHandler['avg'] = average
		GIFRankHandler['iter'] = iterations
		collection.save(GIFRankHandler)

def averageTimeNews(average, iterations):
	NEWSRankHandler = collection.find_one({"name": "NEWSRankHandler"})
	if NEWSRankHandler is None:
		NEWSRankHandler = {'avg': average, 'iter': iterations}
		collection.insert(NEWSRankHandler)
	else:
		NEWSRankHandler['avg'] = average
		NEWSRankHandler['iter'] = iterations
		collection.save(NEWSRankHandler)

def getGIF():
	GIFRankHandler = collection.find_one({"name": "GIFRankHandler"})
	if GIFRankHandler is None:
		return {'avg': 0.5, 'iter': 1}
	return {'avg': GIFRankHandler['avg'], 'iter': GIFRankHandler['iter']}

def getNews():
	NEWSRankHandler = collection.find_one({"name": "NEWSRankHandler"})
	if NEWSRankHandler is None:
		return {'avg': 0.5, 'iter': 1}
	return {'avg': NEWSRankHandler['avg'], 'iter': NEWSRankHandler['iter']}