from boost import weights

class giphyModel(object):
	
	def __init__(self, result):
		self.id = result.id
		self.url = result.url
		self.height = result.height
		self.width = result.width
		self.media_url = result.media_url
		
	# scores the GIF
	def score(self, score):
		weights.weight += score
		weights.iterations += 1
		return (score * weights.weighing['giphy'])

	def getImageList(self):
		dictionary = {}
		dictionary['score'] = self.score(weights.average)
		dictionary['media_url'] = self.media_url
		return dictionary