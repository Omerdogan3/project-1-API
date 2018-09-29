import subprocess
from bottle import run, post, request, response, get, route, hook
from Universe import *
from Probe import *

# @route('/<path>',method = 'GET')
# def process(path):
# 	return subprocess.check_output(['python',path+'.py'],shell=True)
# run(host='localhost', port=8080, debug=True)

@hook('after_request')
def enable_cors():
    """
    You need to add some headers to each request.
    Don't use the wildcard '*' for Access-Control-Allow-Origin in production.
    """
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

uni = Universe(30)

@route('/')
def main():
	from bottle import response
	from json import dumps
	uni.printUniverse()
	starData = uni.getStarData()
	coordinates = uni.getCoordinates()
	response.content_type = 'application/json'
	return dumps({"starData": starData, "coordinates": coordinates})

@route('/search')
def searhIndex():
	from bottle import response
	from json import dumps
	probe = Probe(uni)
	response.content_type = 'application/json'
	return dumps(probe.searchStepByStep())
run(host='localhost', port=8080, debug=True)
