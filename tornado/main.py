#!/usr/bin/env python
import tornado.escape
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.websocket
import os.path
from tornado.options import define, options
# non tornado
from networks import reddit, giphy, tumblr
import unicodedata

define("port", default = 8000, help = "run on the given port", type = int)
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/api/giphy.json/(?P<param1>[^\/]+)/?(?P<param2>[^\/]+)?", GiphyAPIHandler),
            (r"/api/redditImage.json", RedditWholeHandler),
            (r"/api/reddit.json", RedditWholeHandler),
            (r"/api/tumblrImage", TumblrWholeHandler),
        ]
        settings = dict(
            cookie_secret = " 8SGUe0QKS/ecvBl5WSYLw36RuNPtqEenqkIlAD0BoSY=",
            template_path = os.path.join(os.path.dirname(__file__), "templates"),
            static_path = os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies = True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)

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
    def post(self, param1, param2):
        modelOrWhole = param1
        searchQuery = param2
        if modelOrWhole == 'model':
            giphyImage = giphy.giphy()
            searchQuery = self.get_argument('search', '')
            data = giphyImage.getImage(searchQuery, 'whole')
            if searchQuery:
                login_response = {
                    'error': False, 
                    'msg': data
                }
            else:
                login_response = {
                    'error': True, 
                    'msg': 'Please enter a Search Query'
                }
            self.write(login_response)
        else:
            giphyImage = giphy.giphy()
            searchQuery = self.get_argument('search', '')
            data = giphyImage.getImage(searchQuery, 'whole')
            if searchQuery:
                login_response = {
                    'error': False, 
                    'msg': data
                }
            else:
                login_response = {
                    'error': True, 
                    'msg': 'Please enter a Search Query'
                }
            self.write(login_response)

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