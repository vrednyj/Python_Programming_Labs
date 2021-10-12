# -------------------------------------------------------------------------------
# Name:        Lab4_Q3.py
# Project:     Python_Programming_Labs
#
# Author:      Vitaliy Baseckas
#
# Created:     10.10.2021
# Copyright:   (c) Vitaliy Baseckas 2021
# Licence:     <your licence>
# -------------------------------------------------------------------------------
'''Read in information from the user on the details of a Virtual Machine to be created. Keep in
mind the minimum specification required by each Operating System. Minimum specifications
do not change. The selection of features to be installed should be stored. For each feature a
number of tuning settings should be stored. Consider the date of the request, who made the
request, when is the VM needed by and for how long, etc. Store each of the items of information
in the correct data store. Do not ask the user to enter unnecessary information. Do not provide
greater storage on the VM than requested – no short cuts by standardising on one or two sizes!
Once all of the information is gathered it should be presented back to the user for confirmation
in a tidy manner.'''
import os
import datetime
from time import *

user_db={}
os_selection={}
requirement_list=[]
os_requirements={"Windows 10":16, "Ubuntu":8, "MacOS":32, "OS/2":4}
additional_software={"None":0,"Pycharm":1,"Eclips":2,"Maven":6}

def clear_the_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

user_name=input("Please enter you name:")

clear_the_screen()

order=1

for i in (os_requirements.keys()):
    print("{0} {1}".format(order,i))
    os_selection[order]=str(i)
    order+=1

while 1:
    os_software_selection=input("Please select OS required:")
    if 1:
    #try:
        if os_software_selection.isdigit()== False or int(os_software_selection) >= order:
            print("{}".format("Incorrect key selection. Try again."))
        else:
            requirement_list.append(os_selection[int(os_software_selection)])
            break
    if 1:
    #except:
        pass
clear_the_screen()

order=1
for i in (additional_software.keys()):
    print("{0} {1}".format(order,i))
    os_selection[order]=i
    order+=1

while 1:
    software_selection=input("Please select the software:")
    try:
        if software_selection.isdigit()== False or int(software_selection) >= order:
            print("{}".format("Incorrect key selection. Try again."))
        else:
            requirement_list.append(os_selection[int(software_selection)])
            break
    except:
        pass

clear_the_screen()

while 1:
    date=input("Please enter the required date in format dd/mm/yyyy:")
    try:
        print(date)
        datetime.datetime.strptime(date, "%d/%m/%Y")
        requirement_list.append(date)
        now = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        requirement_list.append(now)
        break
    except:
        print("{}".format("Incorrect date format. Try again."))
        pass

clear_the_screen()

requirement_list.append(os_requirements[requirement_list[0]]+additional_software[requirement_list[1]])
user_db[user_name]=requirement_list
print("The user {0} has requested on {1}\nthe following software: {2} and {3} to use before "
      "{4} date.\nThis configuration requires of {5} RAM of the Virtual Machine.\n "
      .format(user_name, user_db[user_name][3], user_db[user_name][0], user_db[user_name][1],
              user_db[user_name][2], user_db[user_name][4]))


