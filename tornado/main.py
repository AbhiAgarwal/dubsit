#!/usr/bin/env python
import tornado.escape
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.websocket
import newrelic.agent
import os.path
from tornado.options import define, options
from rank.dubrank import GIFRankHandler, NEWSRankHandler
import unicodedata

newrelic.agent.initialize('./newrelic.ini')
define("port", default = 8000, help = "run on the given port", type = int)
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/api/gif/rank/(?P<param1>[^\/]+)?.json", GIFRankHandler),
            (r"/api/news/rank/(?P<param1>[^\/]+)?.json", NEWSRankHandler),
        ]
        settings = dict(
            cookie_secret = "8SGUe0QKS/ecvBl5WSYLw36RuNPtqEenqkIlAD0BoSY=",
            template_path = os.path.join(os.path.dirname(__file__), "templates"),
            static_path = os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies = True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

def main():
    tornado.options.parse_command_line()
    app = Application()
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()