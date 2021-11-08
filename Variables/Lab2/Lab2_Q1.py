# -------------------------------------------------------------------------------
# Name:        Lab2_Q1.py
# Project:     Python_Programming_Labs
#
# Author:      Vitaliy Baseckas
#
# Created:     08.11.2021
# Copyright:   (c) Vitaliy Baseckas 2021
# Licence:     <your licence>
# -------------------------------------------------------------------------------
'''
Question 1:
Store the following statement in a variable named python_mission.
The mission of the Python Software Foundation is to promote, protect,
and advance the Python programming language, and to support and facilitate
the growth of a diverse and international community of Python programmers
• Count the number of appearances of the letter s.
• Find the second instance of the word Python which occurs somewhere after position 25.
Selection structures and loops should not be used. Your answer should only use string methods.
• What value is returned from the statement
print(“The word returned is: {}”.format(python_mission[25:34]))
• Find out if the word ‘diverse’ is in the mission statement using two different methods
• Check if the string “12345” is a number
• Print out the following directory structure as a string
C:\users\ndarby\python3\python-3.5.1\bin
'''


python_mission='''The mission of the Python Software Foundation is to promote, protect,
and advance the Python programming language, and to support and facilitate
the growth of a diverse and international community of Python programmers'''

print(python_mission.lower().count("s")) #Count the number of appearances of the letter s
#-> 7
print(python_mission.find("Python",25)) #Find the second instance of the word Python which occurs somewhere after position 25.
#-> 86
print("The word returned is: {}".format(python_mission[25:34]))
#-> The word returned is:  Software
print(python_mission.find("diverse"))
#-> 161
print("1234".isdigit())
#-> True
print(r"C:\users\ndarby\python3\python-3.5.1\bin")
#-> C:\users\ndarby\python3\python-3.5.1\bin


