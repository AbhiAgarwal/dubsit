from giphypop import Giphy
from imageModels import imageModel, giphyModel
import json

class giphy(object):
	def __init__(self):
		self.allResults = []
		self.currentResult = []
	# this physically gets the image from the server
	def getImage(self, stringQuery, wholeOrimageModel):
		currentResult = [x for x in Giphy().search(stringQuery)]
		self.currentResult = currentResult
		self.allResults.append(currentResult)
		returnList = []
		for i in range(0, len(currentResult)):
			if wholeOrimageModel == 'whole':
				dictionary = self.processImage(currentResult[i])
				returnList.append(dictionary)
			elif wholeOrimageModel == 'model':
				dictionary = self.processModel(currentResult[i])
				returnList.append(dictionary)
		return returnList
	# processes according to the image object, this is to try get all the values
	# of every image in accordance with all the social networks
	def processModel(self, result):
		image = imageModel.imageModel(result)
		return image.getImageList()
	# everything is stored as a giphy object, this is to try to get all the
	# values out before parsing it into the engine
	def processImage(self, result):
		image = giphyModel.giphyModel(result)
		return image.getImageList()