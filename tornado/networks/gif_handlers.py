#!/usr/bin/env python
import tornado.escape
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.websocket
import os.path
from tornado.options import define, options
from networks import gif_reddit, gif_giphy, gif_tumblr
import unicodedata
from boost.timing import timeit
from boost import timing
from boost.timeout import timeout

# Whole: Raw data of all the images given by Social Network on that topic.
# Model: Sorted data of all the images given by the different social networks 
# according to our pre-defined Model.

# @Desc: Handles the 'whole' and 'model' Giphy API requests
# @Param: 2 parameters, 
# Param1: either querying a model or the whole unparsed data, ie: 'Whole'
# Param2: the actual name of the request, ie: 'Pokemon'
# @Return: JSON from Giphy parsed either 'model' or 'whole' way.

@timeit
@timeout(timing.GiphyGIFAPI['avg'] + 5)
def GiphyGIFAPI(modelOrWhole, query):
    if modelOrWhole == 'model':
        # Starting Giphy Optimization
        giphyImage = gif_giphy.giphy()
        data = giphyImage.getImage(query, 'model')
        return data
    else:
        # Starting Giphy Optimization
        giphyImage = gif_giphy.giphy()
        data = giphyImage.getImage(query, 'whole')
        return data

@timeit
@timeout(timing.RedditGIFAPI['avg'] + 5)
def RedditGIFAPI(modelOrWhole, query):
    if modelOrWhole == 'model':
        # Starting Reddit Optimization
        redditImage = gif_reddit.reddit()
        data = redditImage.getImage(query, 'model')
        return data
    else:
        # Starting Reddit Optimization
        redditImage = gif_reddit.reddit()
        data = redditImage.getImage(query, 'whole')
        return data

@timeit
@timeout(timing.TumblrGIFAPI['avg'] + 5)
def TumblrGIFAPI(modelOrWhole, query):
    if modelOrWhole == 'model':
        tumblrImage = gif_tumblr.tumblr()
        tumblrImage.getImage()
        return {}
    else:
        tumblrImage = gif_tumblr.tumblr()
        tumblrImage.getImage()
        return {}       