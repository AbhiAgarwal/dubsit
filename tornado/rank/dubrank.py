#!/usr/bin/env python
import tornado.escape
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.websocket
import os.path
from tornado.options import define, options
from operator import itemgetter
import unicodedata, sys, json
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
    	GiphyResults = GiphyGIFAPI('model', query)
    	RedditResults = RedditGIFAPI('model', query)
    	TotalResults = self.GIFRank(GiphyResults, RedditResults)
        self.write(tornado.escape.json_encode(TotalResults))

    def GIFRank(self, GiphyResults, RedditResults):
        finalSource = [];

        # parse through Giphy Results
        for i in GiphyResults:
            i['score'] = 0.7

            # delete source element
            del i['source']
            del i['id']
            del i['url']
            del i['height']
            del i['width']
            # append the result
            finalSource.append(i)

        # parse through Reddit Results
        for i in RedditResults:
            i['score'] = 1

            # delete source private details
            del i['source']
            del i['id']
            del i['ups']
            del i['downs']
            del i['num_comments']
            del i['url']
            # append the result
            finalSource.append(i)   

        finalSource = (sorted(finalSource,key=itemgetter('score')))[::-1]

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