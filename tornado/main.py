#!/usr/bin/env python
import tornado.escape
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.websocket
import os.path
from tornado.options import define, options
from networks import reddit, giphy
import unicodedata

define("port", default = 8000, help = "run on the given port", type = int)
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/apisource/giphyImage.json/([^/]+)", GiphyHandler),
            (r"/apisource/redditImage.json", RedditHandler),
        ]
        settings = dict(
            cookie_secret = " 8SGUe0QKS/ecvBl5WSYLw36RuNPtqEenqkIlAD0BoSY=",
            template_path = os.path.join(os.path.dirname(__file__), "templates"),
            static_path = os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies = True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)

class GiphyHandler(tornado.web.RequestHandler):
    def get(self, searchQuery):
        # Querying search
        query = unicodedata.normalize('NFKD', searchQuery).encode('ascii','ignore')
        splitArray = query.split()
        query = " ".join(splitArray)
        # Starting Giphy Optimization
        giphyImage = giphy.giphy()
        data = giphyImage.getImage(query)
        self.set_header('Content-Type', 'text/javascript')
        self.write(tornado.escape.json_encode(data))
    def post(self):
        giphyImage = giphy.giphy()
        searchQuery = self.get_argument('search', '')
        data = giphyImage.getImage(searchQuery)
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

class RedditHandler(tornado.web.RequestHandler):
    def get(self):
        redditImage = reddit.reddit(),
        data = redditImage.getImage("test")
        self.set_header('Content-Type', 'text/javascript')
        self.write(tornado.escape.json_encode(data))

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