#!/usr/bin/env python
#Brady R. Cornett
#Script for getting API data about the weather
#Uses local postal code to get data from API

import yaml, requests, sys, os, json, datetime, calendar
sys.path.append(os.path.abspath("/home/brady/workspace/python"))
from datetime import datetime
from pyMail import sendEmail
from pyLog import log

#Function for checking response codes from API Calls
def check(statusCode, apiName):
	if (statusCode != 200):
		log("Invalid Status Code Returned From "+apiName+": "+statusCode, logpath, logname, "ERROR")
		errorEmail("Invalid Status Code Returned From "+apiName+": "+str(statusCode))
		sys.exit(1)

#Function for sending error emails for multiple things
def errorEmail(errorString):
	subj = "ERROR - Daily Weather Email"
	sendEmail(cfg['errorDistro'], subj, errorString)

#Function for computing date provided from API into day of the week
def calculateDay(date):
	log("Processing input date: "+date, logpath, logname)
	newDate = str(date[8:10])
	newDate = str(newDate+" "+date[5:7])
	newDate = str(newDate+" " +date[0:4])
	day = datetime.strptime(newDate, '%d %m %Y').weekday() 
	return (calendar.day_name[day]) 

#Function for parsing each days forecast data
def parseForecastData(forecast):
	finalForecast = "<h1 style='text-align:center;'>5 Day Forecast</h1><hr>"
	for i in range(5):
		day = calculateDay(str(forecast['DailyForecasts'][i]['Date'])[0:10])
		finalForecast = finalForecast + "<h2>"+day+": "+str(forecast['DailyForecasts'][i]['Date'])[0:10]+"</h2>"
		finalForecast = finalForecast + "<p>&nbsp;&nbsp;Max: "+str(forecast['DailyForecasts'][i]['Temperature']['Maximum']['Value'])+"&nbsp;&nbsp;"+" Min: "+str(forecast['DailyForecasts'][i]['Temperature']['Minimum']['Value'])+"</p>"
		finalForecast = finalForecast + "<h3>Day time:</h3>"
		finalForecast = finalForecast + "<p>&nbsp;&nbsp;Precipitation: "+str(forecast['DailyForecasts'][i]['Day']['HasPrecipitation'])+"<br>&nbsp;&nbsp;"+"Weather: "+str(forecast['DailyForecasts'][i]['Day']['IconPhrase'])+"</p>"
		finalForecast = finalForecast + "<h3>Night time:</h3>"
		finalForecast = finalForecast + "<p>&nbsp;&nbsp;Precipitation: "+str(forecast['DailyForecasts'][i]['Night']['HasPrecipitation'])+"<br>&nbsp;&nbsp;"+"Weather: "+str(forecast['DailyForecasts'][i]['Night']['IconPhrase'])+"</p><br>"
	return finalForecast



if (os.path.exists('/home/brady/workspace/cfgfiles/weatherAPI.yml')):
	with open('/home/brady/workspace/cfgfiles/weatherAPI.yml') as f:
		cfg = yaml.safe_load(f)
		key = cfg['key']
		logpath = cfg['logpath']
		logname = cfg['logname']
	log("Config file sourced.", logpath, logname)
	if(len(sys.argv) != 2):
		log("Invalid number of arguments", logpath, logname, "ERROR")	
		sys.exit(1)
		errorEmail("Invalid number of arguments provided")
	postal = sys.argv[1]

	#Reaching out to grab locations key for weather data
	log("Reaching out to Locations API", logpath, logname)
	params = {'q':postal,'apikey':key}
	url = 'http://dataservice.accuweather.com/locations/v1/postalcodes/us/search'
	headers = {'Accept-Encoding': 'gzip,deflate'}
	locationResponse = requests.get(url, params=params, headers=headers)
	check(locationResponse.status_code, "Location API")
	locationData = json.loads(locationResponse.text)[0]

	#Reaching out to get current weather data
	log("Reaching out to Current Conditions API", logpath, logname)
	params = {'apikey':key}
	url = 'http://dataservice.accuweather.com/currentconditions/v1/'+locationData['Key']
	currConditionsResponse = requests.get(url, params=params, headers=headers)
	check(currConditionsResponse.status_code, "Current Conditions API")
	currCondsData = json.loads(currConditionsResponse.text)[0]

	#Reaching out to get future forecast data
	log("Reaching out to 5 Day Forecast API", logpath, logname)
	url = 'http://dataservice.accuweather.com/forecasts/v1/daily/5day/'+locationData['Key']
	forecastResponse = requests.get(url, params=params, headers=headers)
	check(forecastResponse.status_code, "Forecast API")
	forecast = json.loads(forecastResponse.text)
	forecast = parseForecastData(forecast)

	currCondsContent = "<h1 style='text-align:center;'>CURRENT CONDITIONS</h1>"
	currCondsContent = currCondsContent + "<hr><h3>Temp: "+str(currCondsData['Temperature']['Imperial']['Value'])+"</h3><h3>Weather: "+currCondsData['WeatherText']+"</h3><h3>Precipitation: "+str(currCondsData['PrecipitationType'])+"</h3>"

	now = datetime.now()
	log("Sending daily email", logpath, logname)
	subj = "Daily Weather Email 0" + str(now.month)+"/"+str(now.day)+"/"+str(now.year)
	sendEmail(cfg['recipients'], subj, currCondsContent+forecast) 
else:
	print("CONFIG FILE NOT FOUND. EXITING")
	errorEmail("CONFIG FILE NOT FOUND")
	sys.exit(1)
