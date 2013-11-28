class giphyModel(object):
	
	def __init__(self, result):
		self.id = result.id
		self.type = result.type
		self.url = result.url
		self.raw_data = result.raw_data
		self.fullscreen = result.fullscreen
		self.tiled = result.tiled
		self.bitly = result.bitly
		self.media_url = result.media_url
		self.frames = result.frames
		self.height = result.height
		self.width = result.width
		self.fixed_height = result.fixed_height
		self.fixed_width = result.fixed_width

	def getImageList(self):
		dictionary = {}
		dictionary['id'] = self.id
		dictionary['type'] = self.type
		dictionary['url'] = self.url
		dictionary['raw_data'] = self.raw_data
		dictionary['fullscreen'] = self.fullscreen
		dictionary['tiled'] = self.tiled
		dictionary['bitly'] = self.bitly
		dictionary['media_url'] = self.media_url
		dictionary['frames'] = self.frames
		dictionary['height'] = self.height
		dictionary['width'] = self.width
		dictionary['fixed_height'] = self.fixed_height
		dictionary['fixed_width'] = self.fixed_width
		return dictionary