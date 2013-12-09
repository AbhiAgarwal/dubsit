#!/usr/bin/env python
# tornado configurations
import tornado.escape
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.websocket
import os.path
from operator import itemgetter
from tornado.options import define, options
# personal calls
from networks.gif_handlers import GiphyGIFAPI, RedditGIFAPI, TumblrGIFAPI
from networks.news_handlers import RedditNEWSAPI
# Timing Functions
from boost.timing import timeit
from boost import timing
from boost.timeout import timeout
# mongo
from mongo import tags
# normalize
from boost.normalize import normalize

@timeit
@timeout((timing.GIFRankHandler['avg'] + 10))
class GIFRankHandler(tornado.web.RequestHandler):

    def get(self, param1):
    	# Querying search
        query = normalize(param1)
        # Get Results
        tags.GIFSearch(query)
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
        # reset
        result = [dict(tupleized) for tupleized in set(tuple(item.items()) for item in finalSource)]
        # sort the final source before saving as JSON
        finalSource = (sorted(result, key = itemgetter('score')))[::-1]
        # return the source to be shown
        return finalSource

@timeit
@timeout(timing.GIFRankHandler['avg'] + 10)
class NEWSRankHandler(tornado.web.RequestHandler):

    def get(self, param1):
        # Querying search
        query = normalize(param1)
        tags.NewsSearch(query)
		# Get Results
        RedditResults = RedditNEWSAPI('model', query)
        TotalResults = self.NEWSRank(RedditResults)
        self.write(tornado.escape.json_encode(TotalResults))

    def NEWSRank(self, RedditResults):
        finalSource = []; # array to return
        # parse through Reddit Results
        for i in RedditResults: finalSource.append(i)
        # reset
        result = [dict(tupleized) for tupleized in set(tuple(item.items()) for item in finalSource)]
        # sort the final source before saving as JSON
        finalSource = (sorted(result, key = itemgetter('score')))[::-1]
        # return the source to be shown
        return finalSource
