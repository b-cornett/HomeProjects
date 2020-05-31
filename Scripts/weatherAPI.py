#!/usr/bin/env python
#Brady R. Cornett
#Script for getting API data about the weather
#Uses local postal code to get data from API

import yaml, requests, sys, os, json
sys.path.append(os.path.abspath("/home/brady/workspace/python"))
from pyMail import sendEmail

if (os.path.exists('/home/brady/workspace/cfgfiles/email.yml')):
        print("Sourcing Config File")
        with open('/home/brady/workspace/cfgfiles/weatherAPI.yml') as f:
                cfg = yaml.safe_load(f)
                key = cfg['key']
                postal = cfg['postal']
        params = {'q':postal,'apikey':key}
        url = 'http://dataservice.accuweather.com/locations/v1/postalcodes/us/search'
        headers = {'Accept-Encoding': 'gzip,deflate'}
        print("Reaching out to Locations API")
        response = requests.get(url, params=params, headers=headers)
        data = json.loads(response.text)[0]
        params = {'apikey':key}
        url = 'http://dataservice.accuweather.com/currentconditions/v1/'+data['Key']
        headers = {'Accept-Encoding': 'gzip,deflate'}
        print("Reaching out to Current Conditions API")
        response = requests.get(url, params=params, headers=headers)
        currConds = json.loads(response.text)[0]
        content = "CURRENT CONDITIONS:\n========================\nTemp: "+str(currConds['Temperature']['Imperial']['Value'])+"\nWeather: "+currConds['WeatherText']+"\nPrecipitation: "+st
r(currConds['PrecipitationType'])+"\n========================\n\n"



        sendEmail(cfg['recipients'], "Daily Weather Email", content)
else:
        print("Config file not available. Exiting.")
        sys.exit(1)