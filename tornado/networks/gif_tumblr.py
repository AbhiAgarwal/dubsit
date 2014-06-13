import pytumblr
import json

class tumblr(object):

	allResults = []
	currentResult = []
	client = pytumblr.TumblrRestClient(
	    '',
	    '',
	    '',
	    '',
	)

	def __init__(self):
		allResults = []
		currentResult = []

	# this physically gets the image from the server
	def getImage(self):
		#self.client.info()
		pass
