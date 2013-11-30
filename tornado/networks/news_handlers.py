#!/usr/bin/env python
import tornado.escape
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.websocket
import os.path
from tornado.options import define, options
from networks import news_reddit
import unicodedata

def RedditNEWSAPI(modelOrWhole, query):
    if modelOrWhole == 'model':
        # Starting Reddit News Optimization
        redditNews = news_reddit.reddit()
        data = redditNews.getNews(query, 'model')
        return data
    else:
        # Starting Reddit News Optimization
        redditNews = news_reddit.reddit()
        data = redditNews.getNews(query, 'whole')
        return data