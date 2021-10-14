# -------------------------------------------------------------------------------
# Name:         Lab2_Q2.py
# Purpose:
#
# Author:      Vitaliy Baseckas
#
# Created:     08.10.2021
# Copyright:   (c) Vitaliy Baseckas 2021
# Licence:     <your licence>
# -------------------------------------------------------------------------------
'''
From the python_mission string indicated in the previous question find the last instance of the word
Python. Use only string methods and variables to carry out this task. Do not use loops or selection
structures
'''
python_mission='''The mission of the Python Software Foundation is to promote, protect,
and advance the Python programming language, and to support and facilitate
the growth of a diverse and international community of Python programmers'''

print("The last instance of the word Python is: {}".format(python_mission.rfind("Python")))
#string.rfind() starts searching from the end
