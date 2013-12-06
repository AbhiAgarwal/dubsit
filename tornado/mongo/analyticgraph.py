#!/usr/bin/env python
# tornado configurations
import tornado.escape
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.websocket
import os.path
import unicodedata, sys, json
from operator import itemgetter
from tornado.options import define, options
# operations
import os
import datetime
# normalize
from boost.normalize import normalize
# Mongo
import pymongo
from pymongo import MongoClient
 
#MONGO_URL = 'mongodb://tornado:pT3mW49P81u@widmore.mongohq.com:10010/Dubsit'
client = MongoClient()

db = client.Dubsit
GIFcollection = db.GIFsearches
NEWScollection = db.NEWSsearches

class AnalyticHandler(tornado.web.RequestHandler):

    def get(self, param1):
    	# Querying search
        query = normalize(param1)
        # Get Results
        result = []
        if 'gif' in query:
            toReturn = GIFcollection.find().sort("count").limit(7)
            for doc in toReturn:
                result.append({'count': doc['count'], 'name': doc['name']})
        elif query is 'news':
            toReturn = GIFcollection.find().sort("count").limit(7)
            for doc in toReturn:
                result.append({'count': doc['count'], 'name': doc['name']})

        self.write(tornado.escape.json_encode(result))