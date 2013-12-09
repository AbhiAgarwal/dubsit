from networksRank import reddit

class redditModel(object):

	def __init__(self, result):
		self.id = result.get('name')
		self.url = result.get('url')
		self.num_comments = result.get('num_comments')
		self.ups = result.get('ups')
		self.downs = result.get('downs')
		self.media_url = result.get('url')

	def getImageList(self):
		dictionary = {}
		dictionary['score'] = reddit.GIFscore(self.ups, self.downs, self.num_comments)
		dictionary['media_url'] = self.media_url
		return dictionary
