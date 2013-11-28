#!/usr/bin/env python
import tornado.escape
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.websocket
import os.path
from tornado.options import define, options
import unicodedata

class GIFRankHandler(tornado.web.RequestHandler):
    def get(self, param1):
        self.write(tornado.escape.json_encode({'hello': 5}))