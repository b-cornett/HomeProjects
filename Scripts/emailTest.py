#!/usr/bin/env python
#Brady R. Cornett
#Script for testing the pyMail.py script
#02/15/2020

import os
import sys
sys.path.append(os.path.abspath("/home/brady/workspace/python"))
from pyMail import sendEmail

sendEmail("TestSub", "TestText")
