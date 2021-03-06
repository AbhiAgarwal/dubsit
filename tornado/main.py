#!/usr/bin/env python
import tornado.escape
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.websocket
import tornado.auth
import newrelic.agent
import os.path
from tornado.options import define, options
from rank.dubrank import GIFRankHandler, NEWSRankHandler
from mongo.analyticgraph import AnalyticHandler
from mongo import relevance
#from feed.facebook import FacebookOAuth, FacebookAuthLoginHandler, FacebookAuthLogoutHandler
#from feed.twitter import TwitterHandler, TwitterLogoutHandler
import unicodedata

newrelic.agent.initialize('./newrelic.ini')
define("port", default = 8000, help = "run on the given port", type = int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            # API Decleration
            (r"/api/gif/rank/(?P<param1>[^\/]+)?.json", GIFRankHandler),
            (r"/api/news/rank/(?P<param1>[^\/]+)?.json", NEWSRankHandler),
            (r"/api/graph/(?P<param1>[^\/]+)?.json", AnalyticHandler),
        ]
        settings = dict(
            cookie_secret = "",
            template_path = os.path.join(os.path.dirname(__file__), "templates"),
            static_path = os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies = True,
            facebook_api_key = "",
            facebook_secret = "",
            twitter_consumer_key = "",
            twitter_consumer_secret = "",
        )
        tornado.web.Application.__init__(self, handlers, **settings)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_header("Content-Type", "text/html; charset=UTF-8")
        self.set_header("Cache-control", "content=public")
        self.set_header("Cache-control", "max-age=25200")
        self.render("index.html", relevance=relevance.GIF)

def main():
    tornado.options.parse_command_line()
    app = Application()
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
