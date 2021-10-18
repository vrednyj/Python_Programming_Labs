# -------------------------------------------------------------------------------
# Name:        Lab5_Q2.py
# Project:     Python_Programming_Labs
#
# Author:      Vitaliy Baseckas
#
# Created:     18.10.2021
# Copyright:   (c) Vitaliy Baseckas 2021
# Licence:     <your licence>
# -------------------------------------------------------------------------------
'''Use the api documentation only to find out information on the necessary functions to carry out the
following tasks. Don’t use youtube! Write a python script to encrypt a password. Use the timeit
function to time it takes to encrypt the data.'''
import timeit
from timeit import Timer
import hashlib


def password_encription(a):
    output = hashlib.sha256(bytes(a, encoding='utf-8')).hexdigest()
    print("The password was encripted to:{}".format(output))

password = input("Please enter your password for encripton:")
t = Timer(lambda: password_encription(password))
return_time=t.timeit(number=1)
print("It took:{} seconds".format(return_time))
