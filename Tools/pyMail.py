#!/usr/bin/env python
#Brady R. Cornett
#Personal Script for sending emails via Python from Raspberry Pi
#02/12/2020

import yaml
import smtplib
import os
import sys

def sendEmail(inpSubject, inpText):
	if (os.path.exists('/home/brady/workspace/cfgfiles/email.yml')):
		with open('/home/brady/workspace/cfgfiles/email.yml') as f:
			cfg = yaml.safe_load(f)
		subject = inpSubject
		text = inpText
		msg = 'Subject: {}\n\n{}'.format(subject,text)
		user = cfg['credentials']['user']
		server = smtplib.SMTP_SSL(cfg['destination']['server'],cfg['destination']['port'])
		server.login(user,cfg['credentials']['password'])
		server.sendmail(user,user,msg)
		server.quit()
	else:
		print('\nUh oh! The config file is missing!\n')
		sys.exit(1)
if __name__ == '__main__':
	print('\nThis script is meant to be sourced through another program Brady you silly.\n')
	sys.exit(0)
