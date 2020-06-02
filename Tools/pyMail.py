#!/usr/bin/env python
#Brady R. Cornett
#Personal Script for sending emails via Python from Raspberry Pi
#Utilizes App Key for google account so I don't have to allow less secure apps :)
#02/12/2020

import yaml
import smtplib
import os
import sys
import yagmail
from email.mime.text import MIMEText
import email.message

def sendEmail(recipients, inpSubject='Test Sub', inpText='Test'):
        if (os.path.exists('/home/brady/workspace/cfgfiles/email.yml')):
                with open('/home/brady/workspace/cfgfiles/email.yml') as f:
                        cfg = yaml.safe_load(f)
                user = cfg['credentials']['user']
                yag = yagmail.SMTP({user:'RaspberryPi'}, cfg['credentials']['password'])
                yag.send(to=recipients, subject=inpSubject, contents=inpText)
        else:
                print('\nUh oh! The config file is missing!\n')
                sys.exit(1)
if __name__ == '__main__':
        print('\nThis script is meant to be sourced through another program Brady you silly.\n')
        sys.exit(0)