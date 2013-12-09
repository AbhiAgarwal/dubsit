import json, requests, sys
from imageModels import gif_redditModel

class reddit(object):

	def __init__(self):
		self.allResults = []
		self.currentResult = []
		self.getGIFSubreddit = 'http://www.reddit.com/r/{}/search.json?q={}&sort=new&restrict_sr=true'
		self.setSubreddits = ['gifs', 'perfectloops']

	# this physically gets the image from the server
	def getSubImage(self, wholeOrimageModel, URL):
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
		image = gif_redditModel.redditModel(result)
		return image.getImageList()

	def getImage(self, stringQuery, wholeOrimageModel):
		returnList = []
		for i in self.setSubreddits:
			URL = (self.getGIFSubreddit).format(i, stringQuery)
			returnInLoop = self.getSubImage(wholeOrimageModel, URL)
			returnList += returnInLoop
		return returnList
