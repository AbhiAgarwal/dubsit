import json, requests, sys
from imageModels import news_redditModel

class reddit(object):
	
	def __init__(self):
		self.allResults = []
		self.currentResult = []
		self.getNewsSubreddit = 'http://www.reddit.com/r/{}/search.json?q={}&sort=new&restrict_sr=true'
		self.setSubreddits = ['news', 'worldnews', 'upliftingnews']

	# this physically gets the news from the server
	def getSubNews(self, wholeOrimageModel, URL):
		requestGIFSubreddit = requests.get(URL)
		self.currentResult = [x for x in requestGIFSubreddit.json()['data']['children']]
		self.allResults.append(self.currentResult)
		returnList = []
		if wholeOrimageModel == 'whole':
			return self.currentResult
		for i in range(0, len(self.currentResult)):
			dictionary = self.processModel(self.currentResult[i]['data'])
			returnList.append(dictionary)
		return returnList

	# everything is stored as a reddit model object, this is to try to get all the
	# values out before parsing it into the engine
	def processModel(self, result):
		image = news_redditModel.redditModel(result)
		return image.getNewsList()

	def getNews(self, stringQuery, wholeOrimageModel):
		returnList = []
		for i in self.setSubreddits:
			URL = (self.getNewsSubreddit).format(i, stringQuery)
			returnInLoop = self.getSubNews(wholeOrimageModel, URL)
			returnList += returnInLoop
		return returnList