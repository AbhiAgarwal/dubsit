#!/usr/bin/env python
import tornado.escape
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.websocket
import os.path
import unicodedata, sys, json
from operator import itemgetter
from tornado.options import define, options
from networks.gif_handlers import GiphyGIFAPI, RedditGIFAPI, TumblrGIFAPI
from networks.news_handlers import RedditNEWSAPI

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
        RedditResults = RedditGIFAPI('model', query)
    	GiphyResults = GiphyGIFAPI('model', query)
    	TotalResults = self.GIFRank(GiphyResults, RedditResults)
        self.write(tornado.escape.json_encode(TotalResults))

    def GIFRank(self, GiphyResults, RedditResults):
        finalSource = []; # array to return
        # parse through Reddit Results
        for i in RedditResults: finalSource.append(i)   
        # parse through Giphy Results
        for i in GiphyResults: finalSource.append(i)   
        # sort the final source before saving as JSON
        finalSource = (sorted(finalSource, key = itemgetter('score')))[::-1]
        # return the source to be shown
        return finalSource

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