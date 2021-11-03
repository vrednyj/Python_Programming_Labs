# -------------------------------------------------------------------------------
# Name:        Lab6_Q1.py
# Project:     Python_Programming_Labs
#
# Author:      Vitaliy Baseckas
#
# Created:     25.10.2021
# Copyright:   (c) Vitaliy Baseckas 2021
# Licence:     <your licence>
# -------------------------------------------------------------------------------
'''The following code sums up the file sizes in a specified directory. Manipulate this code to allow the
user to enter the name of the directory. Check if the directory exists. If it does carry out the addition.
If not exit the program with a user defined warning'''

import os
def practice_q(dir_for_search):
     """
     Practice Question for File Handling
     :return:
     """
     total_size = 0
     #for file_name in os.listdir('C:\\zipDemo'):
     if os.path.exists(dir_for_search):
         for file_name in os.listdir(dir_for_search):
             print(f"{file_name}")
             size = os.path.getsize(os.path.join(dir_for_search, file_name))
             total_size = total_size + size
         print("The contents of this directory is: {}".format(total_size))
     else:
         print("Such folder {0} does not exist".format(dir_for_search))

dir_for_search=input("Please enter the directory for search:")
practice_q(dir_for_search)