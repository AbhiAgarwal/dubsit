build:
	uglifyjs -o ./tornado/static/to_js/dubsit.js ./tornado/static/to_js/dubsit.max.js
	uglifyjs -o ./tornado/static/to_js/app.js ./tornado/static/to_js/app.max.js
	uglifyjs -o ./tornado/static/to_js/jquery.tagsinput.js ./tornado/static/to_js/jquery.tagsinput.max.js
	uglifyjs -o ./tornado/static/to_js/purl.js ./tornado/static/to_js/purl.max.js
	crammit -c assets.yaml

.PHONY: build

minifyagain:
	uglifyjs -o ./tornado/static/serve/dubsit.min.js ./tornado/static/serve/dubsit-fa790b258db0496e88ca7bfbda5d1221cb49d156.min.js
