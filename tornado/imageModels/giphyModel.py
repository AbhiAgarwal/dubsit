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
		# variable width @ 200px height
		self.fixed_height = result.fixed_height
		# - self.fixed_height_url = result.fixed_height.url
		# - self.fixed_height_width = result.fixed_height.width
		# - self.fixed_height_height = result.fixed_height.height
		# - self.fixed_height_downsampled.url = result.fixed_height.downsampled.url
		# - self.fixed_height_downsampled.width = result.fixed_height.downsampled.width
		# - self.fixed_height_downsampled.height = result.fixed_height.downsampled.height
		# - self.fixed_height_still.url = result.fixed_height.still.url
		# - self.fixed_height_still.width = result.fixed_height.still.width
		# - self.fixed_height_still.height = result.fixed_height.still.height
		# variable height @ 200px width
		self.fixed_width = result.fixed_width
		# - self.fixed_width.url = result.fixed_width.url
		# - self.fixed_width.width = result.fixed_width.width
		# - self.fixed_width.height = result.fixed_width.height
		# - self.fixed_width.downsampled.url = result.fixed_width.downsampled.url
		# - self.fixed_width.downsampled.width = result.fixed_width.downsampled.width
		# - self.fixed_width.downsampled.height = result.fixed_width.downsampled.height
		# - self.fixed_width.still.url = result.fixed_width.still.url
		# - self.fixed_width.still.width = result.fixed_width.still.width
		# - self.fixed_width.still.height = result.fixed_width.still.height

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