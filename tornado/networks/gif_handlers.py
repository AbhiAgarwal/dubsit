#!/usr/bin/env python
import tornado.escape
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.websocket
import os.path
from tornado.options import define, options
from networks import reddit, giphy, tumblr
import unicodedata

# Whole: Raw data of all the images given by Social Network on that topic.
# Model: Sorted data of all the images given by the different social networks 
# according to our pre-defined Model.

# @Desc: Handles the 'whole' and 'model' Giphy API requests
# @Param: 2 parameters, 
# Param1: either querying a model or the whole unparsed data, ie: 'Whole'
# Param2: the actual name of the request, ie: 'Pokemon'
# @Return: JSON from Giphy parsed either 'model' or 'whole' way.
class GiphyAPIHandler(tornado.web.RequestHandler):
    def get(self, param1, param2):
        modelOrWhole = param1
        searchQuery = param2
        if modelOrWhole == 'model':
            # Querying search
            query = unicodedata.normalize('NFKD', searchQuery).encode('ascii','ignore')
            splitArray = query.split()
            query = " ".join(splitArray)
            # Starting Giphy Optimization
            giphyImage = giphy.giphy()
            data = giphyImage.getImage(query, 'model')
            self.set_header('Content-Type', 'text/javascript')
            self.write(tornado.escape.json_encode(data))
        else:
            query = unicodedata.normalize('NFKD', searchQuery).encode('ascii','ignore')
            splitArray = query.split()
            query = " ".join(splitArray)
            # Starting Giphy Optimization
            giphyImage = giphy.giphy()
            data = giphyImage.getImage(query, 'whole')
            self.set_header('Content-Type', 'text/javascript')
            self.write(tornado.escape.json_encode(data))

class RedditWholeHandler(tornado.web.RequestHandler):
    def get(self):
        redditImage = reddit.reddit(),
        data = redditImage.getImage("test")
        self.set_header('Content-Type', 'text/javascript')
        self.write(tornado.escape.json_encode(data))

class TumblrWholeHandler(tornado.web.RequestHandler):
    def get(self):
        tumblrImage = tumblr.tumblr()
        tumblrImage.getImage()
        self.render("index.html")