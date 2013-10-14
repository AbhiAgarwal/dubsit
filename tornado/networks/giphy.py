from giphypop import Giphy
import json

class giphy(object):

	allResults = []
	currentResult = []
	APIKey = "dc6zaTOxFJmzC"

	def __init__(self):
		allResults = []
		currentResult = []

	# this physically gets the image from the server
	def getImage(self, stringQuery):
		currentResult = [x for x in Giphy().search(stringQuery)]
		self.currentResult = currentResult
		self.allResults.append(currentResult)
		returnList = []
		for i in range(0, len(currentResult)):
			dictionary = self.processImage(currentResult[i])
			returnList.append(dictionary)
		return returnList

	# everything is stored as a giphy object, this is to try to get all the
	# values out before parsing it into the engine
	def processImage(self, result):
		dictionary = {}
		dictionary['id'] = result.id
		dictionary['type'] = result.type
		dictionary['url'] = result.url
		dictionary['raw_data'] = result.raw_data
		dictionary['fullscreen'] = result.fullscreen
		dictionary['tiled'] = result.tiled
		dictionary['bitly'] = result.bitly
		dictionary['media_url'] = result.media_url
		dictionary['frames'] = result.frames
		dictionary['height'] = result.height
		dictionary['width'] = result.width
		# variable width @ 200px height
		dictionary['fixed_height.url'] = result.fixed_height.url
		dictionary['fixed_height.width'] = result.fixed_height.width
		dictionary['fixed_height.height'] = result.fixed_height.height
		dictionary['fixed_height.downsampled.url'] = result.fixed_height.downsampled.url
		dictionary['fixed_height.downsampled.width'] = result.fixed_height.downsampled.width
		dictionary['fixed_height.downsampled.height'] = result.fixed_height.downsampled.height
		dictionary['fixed_height.still.url'] = result.fixed_height.still.url
		dictionary['fixed_height.still.width'] = result.fixed_height.still.width
		dictionary['fixed_height.still.height'] = result.fixed_height.still.height
		# variable height @ 200px width
		dictionary['fixed_width.url'] = result.fixed_width.url
		dictionary['fixed_width.width'] = result.fixed_width.width
		dictionary['fixed_width.height'] = result.fixed_width.height
		dictionary['fixed_width.downsampled.url'] = result.fixed_width.downsampled.url
		dictionary['fixed_width.downsampled.width'] = result.fixed_width.downsampled.width
		dictionary['fixed_width.downsampled.height'] = result.fixed_width.downsampled.height
		dictionary['fixed_width.still.url'] = result.fixed_width.still.url
		dictionary['fixed_width.still.width'] = result.fixed_width.still.width
		dictionary['fixed_width.still.height'] = result.fixed_width.still.height
		return dictionary