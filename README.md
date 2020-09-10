# HomeProjects  
Repository to store personal projects as I work on them

**WeatherAPI**
- runs every day at 07:00 (Mountain Time) through a Linux crontab
- uses a YML configuration file for most variables
- utilizes custom built pyMail and pyLog modules
- has error reporting through emails
- enter zip code for weather data for specific location
- uses HTML for email for better formatting

Eg: 0 7 * * * /home/brady/workspace/python/weatherAPI.py $POSTAL_CODE >> /tmp/weatherAPI.out 2&>1

(Postal code is manually entered into the crontab)

*Future Updates*

_LOG_  
- 02/12/2020 -- Pushed up first version of pyMail.py  
- 02/15/2020 -- Pushed up emailTest script to test pyMail.py. Also pushing up beginning of weatherAPI.py  
- 05/30/2020 -- Pushed changes to pyMail.py and weatherAPI.py
- 07/18/2020 -- Pushed changes to weatherAPI.py, pushed up pyLog.py. Weather API program now has error emails, checks HTTP response codes, has a commandline argument for zip code and uses logging instead of print statements
- 07/20/2020 -- Pushed final updates to weatherAPI.py. Completed all desired updates.

**MERN-Project**
