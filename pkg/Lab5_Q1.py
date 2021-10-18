# -------------------------------------------------------------------------------
# Name:        Lab5_Q1.py
# Project:     Python_Programming_Labs
#
# Author:      Vitaliy Baseckas
#
# Created:     18.10.2021
# Copyright:   (c) Vitaliy Baseckas 2021
# Licence:     <your licence>
# -------------------------------------------------------------------------------
'''Write a python script to determine the following system information. Import the platform module.
Find out the machine(), node, operating system, current value of the ‘PATH’ and other relevant
configuration variables. Display the information in a tidy manner.'''
import os.path
import platform
import sys

print("{0:<20}:{1:}".format("Node:",platform.node()))
print("{0:<20}:{1:}".format("Operating system",platform.system()))
print("{0:<20s}:{1:}".format("OS Version:",platform.win32_ver()))
print("{0:<20s}:{1:}".format("Platform:",platform.machine()))
print("{0:20s}:{1:}".format("Processor:",platform.processor()))
print("{0:<20s}:{1:}".format("Python Version:",platform.python_version()))
print("{0:<20s}:{1:}".format("Working Path:",str(os.getcwd())))
