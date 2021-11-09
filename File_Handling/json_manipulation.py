# -------------------------------------------------------------------------------
# Name:        json_manipulation.py
# Project:     Python_Programming_Labs
#
# Author:      Vitaliy Baseckas
#
# Created:     09.11.2021
# Copyright:   (c) Vitaliy Baseckas 2021
# Licence:     <your licence>
# -------------------------------------------------------------------------------

import json

person_string = '{"name": "Bob", "languages": "English", "numbers": [2, 1.6, null]}'

# Getting dictionary
person_dict = json.loads(person_string)

# Pretty Printing JSON string back
print(json.dumps(person_dict, indent = 1, sort_keys=True))

import json

# Key:value mapping
student = {
    "Name": "Peter",
    "Roll_no": "0090014",
    "Grade": "A",
    "Age": 20
}
b = json.dumps(student)
#c = json.dump(student) #- dump - write to file
print(b)
#print(c)
