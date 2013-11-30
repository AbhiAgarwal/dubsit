class imageModel(object):
	
	def __init__(self, result):
		self.id = result.id
		self.url = result.url
		self.height = result.height
		self.width = result.width
		self.media_url = result.media_url
		
	def getImageList(self):
		dictionary = {}
		dictionary['id'] = self.id
		dictionary['url'] = self.url
		dictionary['height'] = self.height
		dictionary['width'] = self.width
		dictionary['media_url'] = self.media_url
		dictionary['source'] = 'giphy'
		return dictionary