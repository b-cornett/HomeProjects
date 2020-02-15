#!/usr/bin/env python
#Brady R. Cornett
#Script for getting API data about the weather
#02/15/2020

import yaml, requests, sys, os, json
sys.path.append(os.path.abspath("/home/brady/workspace/python"))
from pyMail import sendEmail

if (os.path.exists('/home/brady/workspace/cfgfiles/email.yml')):
	with open('/home/brady/workspace/cfgfiles/weatherAPI.yml') as f:
		cfg = yaml.safe_load(f)
		key = cfg['key']
		postal = cfg['postal']
	params = {'q':postal,'apikey':key}
	url = 'http://dataservice.accuweather.com/locations/v1/search'
	headers = {'Accept-Encoding': 'gzip,deflate'}
	response = requests.get(url, params=params, headers=headers)
	newKey = response.text[21:29]
else:
	print("Config file not available. Exiting.")
	Sys.exit(1)
