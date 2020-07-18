# HomeProjects  
Repository to store personal projects as I work on them

**WeatherAPI**
- runs every day at 07:00 through a Linux crontab
- uses a YML configuration file for most variables

Eg: 0 7 * * * /home/brady/workspace/python/weatherAPI.py $POSTAL_CODE >> /tmp/weatherAPI.out 2&>1
(Postal code is manually entered into the crontab)

*Future Updates*
* Error Email
* Check HTTP Response
* Crontab Zip Code Manual Input
* HTML Email for formatting
* Logging instead of print statements

_LOG_  
-02/12/2020 -- Pushed up first version of pyMail.py  
-02/15/2020 -- Pushed up emailTest script to test pyMail.py. Also pushing up beginning of weatherAPI.py  
-05/30/2020 -- Pushed changes to pyMail.py and weatherAPI.py
