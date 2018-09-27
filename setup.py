import subprocess
from bottle import run, post, request, response, get, route
from Universe import *

# @route('/<path>',method = 'GET')
# def process(path):
# 	return subprocess.check_output(['python',path+'.py'],shell=True)
# run(host='localhost', port=8080, debug=True)

@route('/')
def main():
	uni = Universe(2**10)
	from bottle import response
	from json import dumps
	uni.printUniverse()
	starData = uni.getStarData()
	coordinates = uni.getCoordinates()
	response.content_type = 'application/json'
	return dumps({"starData": starData, "coordinates": coordinates})
run(host='localhost', port=8080, debug=True)