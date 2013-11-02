class imageModel(object):
	
	def __init__(self, result):
		self.id = result.id
		self.url = result.url
		self.height = result.height
		self.width = result.width
		
	def getImageList(self):
		dictionary = {}
		dictionary['id'] = self.id
		dictionary['url'] = self.url
		dictionary['height'] = self.height
		dictionary['width'] = self.width
		return dictionary