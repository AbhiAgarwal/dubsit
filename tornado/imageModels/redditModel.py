class redditModel(object):
	
	def __init__(self, result):
		self.id = result.get('name')
		self.url = result.get('url')
		self.num_comments = result.get('num_comments')
		self.ups = result.get('ups')
		self.downs = result.get('downs')

	def getImageList(self):
		dictionary = {}
		dictionary['id'] = self.id
		dictionary['url'] = self.url
		dictionary['num_comments'] = self.num_comments
		dictionary['ups'] = self.ups
		dictionary['downs'] = self.downs
		return dictionary