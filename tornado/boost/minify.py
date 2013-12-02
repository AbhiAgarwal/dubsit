from slimit import minify
files = ['jquery-2.0.3.min.js', 'jquery.tagsinput.js', 'bootstrap.min.js', 'jquery.lazyload.min.js', 'least.min.js', 'purl.js', 'jquery.history.js', 'dubsit.js', 'app.js', 'pace.min.js']

def run():
	minified = ""
	for currentFile in files:
		minified += minify(open('../static/js/' + currentFile).read(), mangle=True, mangle_toplevel=True)
	minFile = open('../static/js/main.js', 'w')
	minFile.write(minified)
	minFile.close()

if __name__ == '__main__':
	run()