'''
Created on 2 Oct 2015
Python module to handle app views
'''
#Imports
import requests
from app import app
from flask import render_template
from flask import request
from qpylib import qpylib
from parse import parsePopupInfo

import json

@app.route('/admin')
def admin():
    return render_template("admin_screen.html", title = "Who Is Configuration")
qpylib.log('Server:/admin invoked, returning admin screen...', level='debug')

@app.route('/ip_metadata_provider', methods=['GET'])
def getIPMetadata():
	# Context will be the IP address that is hovered over
	context = request.args.get('context')
	#context = '172.16.194.125'
	qpylib.log('Entering /ip_metadata_provwhois_informationider with context ' + context, level='info')

	try:
		# arin.net seems to use the first value of the ip address (eg. 9 in 9.180.234.11) so we
		# split the ip address on the . and take the first number
		qpylib.log('test output', level='info')
		net1 = context.split('.')[0]
		# The NET-x-0.0.0.1 part of the url
		qpylib.log('test output2', level='info')
		whois_net = 'NET-' + net1 + '-16-0-0-1'

		# The full url, adding in the above NET value + the ip address on the end
		qpylib.log('test output3', level='info')
		endpoint = 'https://whois.arin.net/rest/net/' + whois_net + '/pft?s=' + context

		# Header required to return json
		qpylib.log('test output4', level='info')

		header = { 'Accept' : 'application/json' }
		# The requests library is used to make requests
		qpylib.log('test output 5', level='info')

		response = requests.get(endpoint, headers=header, verify=False)

		qpylib.log('test output6', level='info')
		response_json=response.json()
		#print json
		response_list = parsePopupInfo(response_json)


		# Get the JSON data from the response
		#response_json = response.json()
		#response_json = parsePopupInfo(response.json())

		metadata_dict = {
	                    'key' : 'exampleIPMetadataProvider',
	                    'label' : 'Who Is Information:  ',
	                    'value' : 'Metadata value',
	                    'html' : render_template('metadata_ip.html', whois_information=response_list)
						 }

		return json.dumps(metadata_dict)
	except Exception as e:
		qpylib.log('Something went wrong: ' + str(e), level='error')
