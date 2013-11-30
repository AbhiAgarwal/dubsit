#!/usr/bin/env python
import tornado.escape
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.websocket
import os.path
from tornado.options import define, options
from networks.gif_handlers import GiphyGIFAPI, RedditGIFAPI, TumblrGIFAPI
from networks.news_handlers import RedditNEWSAPI
import unicodedata

def normalize(param1):
    query = unicodedata.normalize('NFKD', param1).encode('ascii','ignore')
    splitArray = query.split()
    query = " ".join(splitArray)
    return query

class GIFRankHandler(tornado.web.RequestHandler):
    def get(self, param1):
    	# Querying search
        query = normalize(param1)
        # Get Results
    	GiphyResults = GiphyGIFAPI('model', query)
    	RedditResults = RedditGIFAPI('model', query)
    	TotalResults = self.GIFRank(GiphyResults, RedditResults)
        self.write(tornado.escape.json_encode(TotalResults))

    def GIFRank(self, GiphyResults, RedditResults):
	   return GiphyResults + RedditResults 

class NEWSRankHandler(tornado.web.RequestHandler):
    def get(self, param1):
        # Querying search
        query = normalize(param1)
		# Get Results
        RedditResults = RedditNEWSAPI('model', query)
        TotalResults = self.NEWSRank(RedditResults)
        self.write(tornado.escape.json_encode(TotalResults))

    def NEWSRank(self, results):
	   return results