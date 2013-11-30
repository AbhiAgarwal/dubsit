from giphypop import Giphy
from imageModels import gif_giphyModel
import json

class giphy(object):
	def __init__(self):
		self.allResults = []
		self.currentResult = []

	# this physically gets the image from the server
	def getImage(self, stringQuery, wholeOrimageModel):
		self.currentResult = [x for x in Giphy().search(stringQuery)]
		self.allResults.append(self.currentResult)
		returnList = []
		if wholeOrimageModel == 'whole':
			return self.currentResult
		for i in range(0, len(self.currentResult)):
			dictionary = self.processModel(self.currentResult[i])
			returnList.append(dictionary)
		return returnList

	# processes according to the giphy model object, this is to try get all the values
	# of every image in accordance with all the social networks
	def processModel(self, result):
		image = gif_giphyModel.imageModel(result)
		return image.getImageList()