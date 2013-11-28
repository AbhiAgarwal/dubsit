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
def GiphyAPI(param1, param2):
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
        return data
    else:
        query = unicodedata.normalize('NFKD', searchQuery).encode('ascii','ignore')
        splitArray = query.split()
        query = " ".join(splitArray)
        # Starting Giphy Optimization
        giphyImage = giphy.giphy()
        data = giphyImage.getImage(query, 'whole')
        return data

def RedditAPI(param1, param2):
    modelOrWhole = param1
    searchQuery = param2
    if modelOrWhole == 'model':
        query = unicodedata.normalize('NFKD', searchQuery).encode('ascii','ignore')
        splitArray = query.split()
        query = " ".join(splitArray)
        # Starting REddit Optimization
        redditImage = reddit.reddit()
        data = redditImage.getImage(param2, 'model')
        return data
    else:
        query = unicodedata.normalize('NFKD', searchQuery).encode('ascii','ignore')
        splitArray = query.split()
        query = " ".join(splitArray)
        # Starting REddit Optimization
        redditImage = reddit.reddit()
        data = redditImage.getImage(param2, 'whole')
        return data

def TumblrAPI(param1, param2):
    tumblrImage = tumblr.tumblr()
    tumblrImage.getImage()
    return {}