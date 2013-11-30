#!/usr/bin/env python
import tornado.escape
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.websocket
import os.path
import unicodedata, sys, json
from math import log
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
    	GiphyResults = GiphyGIFAPI('model', query)
    	RedditResults = RedditGIFAPI('model', query)
    	TotalResults = self.GIFRank(GiphyResults, RedditResults)
        self.write(tornado.escape.json_encode(TotalResults))

    def score(self, ups, downs, comments):
        s = (ups - downs) + comments
        order = log(max(abs(s), 1), 10)
        return order

    def GIFRank(self, GiphyResults, RedditResults):
        weighing = {'reddit': 0.8, 'giphy': 1.0}
        finalSource = []; # array to return
        average = 0 # average scoring

        # parse through Reddit Results
        for i in RedditResults:

            # score reddit
            i['score'] = self.score(i['ups'], i['downs'], i['num_comments'])

            # reddit weighting = 0.8
            i['score'] = i['score'] * weighing['reddit']

            # keep average
            average += i['score']

            # delete source private details
            del i['source'], i['id'], i['ups'], i['downs'], i['num_comments'], i['url']

            # append the result
            finalSource.append(i)

        average = (average/(len(RedditResults)))

        # parse through Giphy Results
        for i in GiphyResults:

            # scoring as average
            i['score'] = average

            # Giphy weighting = 1.0
            i['score'] = i['score'] * weighing['giphy']

            # delete source element
            del i['source']
            del i['id']
            del i['url']
            del i['height']
            del i['width']

            # append the result
            finalSource.append(i)   

        # sort the final source before saving as JSON
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