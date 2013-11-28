#!/usr/bin/env python
import tornado.escape
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.websocket
import os.path
from tornado.options import define, options
from networks.gif_handlers import GiphyAPI, RedditAPI, TumblrAPI
import unicodedata

class GIFRankHandler(tornado.web.RequestHandler):
    def get(self, param1):
    	results = GiphyAPI('model', param1)
        self.write(tornado.escape.json_encode(results))
