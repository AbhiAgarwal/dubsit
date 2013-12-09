from networksRank import reddit

class redditModel(object):

	def __init__(self, result):
		self.id = result.get('name')
		self.url = result.get('url')
		self.num_comments = result.get('num_comments')
		self.ups = result.get('ups')
		self.downs = result.get('downs')
		self.title = result.get('title')

	def getNewsList(self):
		dictionary = {}
		dictionary['url'] = self.url
		dictionary['score'] = reddit.NEWSscore(self.ups, self.downs, self.num_comments)
		dictionary['title'] = self.title
		return dictionary
