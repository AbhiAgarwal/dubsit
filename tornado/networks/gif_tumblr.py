import pytumblr
import json

class tumblr(object):

	allResults = []
	currentResult = []
	client = pytumblr.TumblrRestClient(
	    '5z4ypxsFDNPGlHlDSTaRSdhkIBssuCn4SQNpVYa8dYXtlL6XhM',
	    '8tv32ve6dLQ7DgajsZXtVU64oxC19r5aVKjPKtOqyTvTGMjI3f',
	    'XlM9iYmGQUXT5sVjdYsAZhHQE2oc9uhMJ02TL9pMmWmaqVyQJ9',
	    'upaLJBlpJLmTqGLC3MBTPHMUdMIWfzx43uDiAn4aeCT2V9HtBH',
	)

	def __init__(self):
		allResults = []
		currentResult = []

	# this physically gets the image from the server
	def getImage(self):
		#self.client.info()
		pass