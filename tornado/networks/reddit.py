import json, requests, sys
from imageModels import redditModel

class reddit(object):
	
	def __init__(self):
		self.allResults = []
		self.currentResult = []
		self.getGIFSubreddit = 'http://www.reddit.com/r/gifs/search.json?q={}&sort=new&restrict_sr=true'
	
	# this physically gets the image from the server
	def getImage(self, stringQuery, wholeOrimageModel):
		requestGIFSubreddit = requests.get(self.getGIFSubreddit.format(stringQuery))
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
		image = redditModel.redditModel(result)
		return image.getImageList()