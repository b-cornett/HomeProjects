#!/usr/bin/env python
#Brady R. Cornett
#Personal Script for logging personal python projects
#07/16/2020

import os, sys, datetime, socket

#Function for logging, only allows for INFO or ERROR level. Requires data, filepath and filename variables
def log(data, filepath, filename, level='INFO'):
	if(os.access(filepath, os.W_OK)) is not True:
		print("LOGGING ERROR. Unable to write to specified directory.")
		sys.exit(1)
	else:
		of = open(filepath+filename, "a")
		now=datetime.datetime.now()
		of.write(level+"\t"+now.strftime("%Y-%m-%d %H:%M:%S")+"\t"+socket.gethostname()+"\t"+data+"\n")
		of.close()
	
if __name__ == '__main__':
        print('\nThis script is meant to be sourced through another program Brady you silly.\n')
        sys.exit(0)
