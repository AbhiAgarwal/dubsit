import praw

class reddit(object):

	username = "Dubsit"
	password = "pg9kDaKBQ0Sf0ckxCByijA=="
	r = praw.Reddit(user_agent = 'Dubsit')

	def __init__(self):
		global r
		username = "Dubsit"
		password = "pg9kDaKBQ0Sf0ckxCByijA=="
		r = praw.Reddit(user_agent = 'Dubsit')
		r.login(username, password)

	def getImage(self, stringQuery):
		subreddit = r.get_subreddit('askhistorians')
		print subreddit
		print stringQuery