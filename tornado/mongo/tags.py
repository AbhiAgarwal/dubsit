import os
import datetime
import pymongo
from pymongo import MongoClient

client = MongoClient()

db = client.Dubsit
GIFcollection = db.GIFsearches

def GIFSearch(tag):
	GIFRankHandler = GIFcollection.find_one({'name': tag})
	if GIFRankHandler is None:
		GIFRankHandler = {'name': tag, 'count': 1}
		GIFcollection.insert(GIFRankHandler)
	else:
		GIFRankHandler['count'] += 1
		GIFcollection.save(GIFRankHandler)

NEWScollection = db.NEWSsearches

def NewsSearch(tag):
	NEWSRankHandler = NEWScollection.find_one({'name': tag})
	if NEWSRankHandler is None:
		NEWSRankHandler = {'name': tag, 'count': 1}
		NEWScollection.insert(NEWSRankHandler)
	else:
		NEWSRankHandler['count'] += 1
		NEWScollection.save(NEWSRankHandler)
