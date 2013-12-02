#!/bin/bash

# building the primary configuration
build () {
	uglifyjs -o ./tornado/static/to_js/dubsit.js ./tornado/static/to_js/dubsit.max.js
	uglifyjs -o ./tornado/static/to_js/app.js ./tornado/static/to_js/app.max.js
	uglifyjs -o ./tornado/static/to_js/jquery.tagsinput.js ./tornado/static/to_js/jquery.tagsinput.max.js
	uglifyjs -o ./tornado/static/to_js/purl.js ./tornado/static/to_js/purl.max.js
	crammit -c assets.yaml
	echo "complete"
}

updatejs (){
	uglifyjs -o ./tornado/static/serve/... ./tornado/static/serve/...
}

updatecss (){
	uglifyjs -o ./tornado/static/serve/dubsit-70a5245f99d8721f564cd51b77969717b8215e32.min.css ./tornado/static/serve/dubsit-70a5245f99d8721f564cd51b77969717b8215e32.min.css
}

build