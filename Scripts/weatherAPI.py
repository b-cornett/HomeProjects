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
		log("Invalid Status Code Returned From "+apiName, logpath, logname, "ERROR")
		errorEmail("Invalid Status Code Returned From "+apiName+": "+str(statusCode))
		sys.exit(1)

#Function for sending error emails for multiple things
def errorEmail(errorString):
	subj = "ERROR - Daily Weather Email"
	sendEmail(cfg['errorDistro'], subj, errorString)

#TODO Function for computing date provided from API into day of the week
def calculateDay(date):
	newDate = str(date[9:10])
	print(newDate)
	newDate = str(newDate+" "+date[6:7])
	print(newDate)
	newDate = str(newDate+" " +date[0:4])
	print(newDate)

#Function for parsing each days forecast data
def parseForecastData(forecast):
	finalForecast = "5 Day Forecast:\n========================\n"
	for i in range(5):
		day = calculateDay(str(forecast['DailyForecasts'][i]['Date'])[0:10])
		finalForecast = finalForecast + str(forecast['DailyForecasts'][i]['Date'])[0:10]+"\n"
		finalForecast = finalForecast + "Maximum: "+str(forecast['DailyForecasts'][i]['Temperature']['Maximum']['Value'])+"    "+"Minimum: "+str(forecast['DailyForecasts'][i]['Temperature']['Minimum']['Value'])+"\n"
		finalForecast = finalForecast + "Day:\n"
		finalForecast = finalForecast + "Precipitation: "+str(forecast['DailyForecasts'][i]['Day']['HasPrecipitation'])+"    "+"Weather: "+str(forecast['DailyForecasts'][i]['Day']['IconPhrase'])+"\n"
		finalForecast = finalForecast + "Night:\n"
		finalForecast = finalForecast + "Precipitation: "+str(forecast['DailyForecasts'][i]['Night']['HasPrecipitation'])+"    "+"Weather: "+str(forecast['DailyForecasts'][i]['Night']['IconPhrase'])+"\n\n"
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

	currCondsContent = "CURRENT CONDITIONS:\n========================\nTemp: "+str(currCondsData['Temperature']['Imperial']['Value'])+"\nWeather: "+currCondsData['WeatherText']+"\nPrecipitation: "+str(currCondsData['PrecipitationType'])+"\n========================\n\n"

	now = datetime.now()
	log("Sending daily email", logpath, logname)
	subj = "Daily Weather Email 0" + str(now.month)+"/"+str(now.day)+"/"+str(now.year)
	sendEmail(cfg['recipients'], subj, currCondsContent+forecast) 
else:
	print("CONFIG FILE NOT FOUND. EXITING")
	errorEmail("CONFIG FILE NOT FOUND")
	sys.exit(1)
