class imageModel(object):
	
	def __init__(self, imageID, url, height, width):
		self.imageID = imageID
		self.url = url
		self.height = height
		self.width = width
		
	def getImageList(self):
		dictionary = {}
		dictionary['id'] = self.imageID
		dictionary['url'] = self.url
		dictionary['height'] = self.height
		dictionary['width'] = self.width
		return dictionary