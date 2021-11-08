# -------------------------------------------------------------------------------
# Name:        Variables_2.py
# Project:     Python_Programming_Labs
#
# Author:      Vitaliy Baseckas
#
# Created:     08.11.2021
# Copyright:   (c) Vitaliy Baseckas 2021
# Licence:     <your licence>
# -------------------------------------------------------------------------------

manifesto='''Individuals and interactions over proccesses and tools
Working software over comprehensive documentation
Customer collaboration over contract negotiation
Responding to change over dollowing a plan'''

over=manifesto.count("over")
print("The word over appears {} time in the agile manifesto".format(over))

small=manifesto.lower()
no_of_os=manifesto.count('o')
print("The latter o appears {} time in the manifesto".format(no_of_os))


title="Invoce Screen"
print(title.rjust(30, ' '))
title2="Customer: Vitaliy Baseckas"
print("{:>30s}".format(title2))
print("\n"*2)
price1=99.99
price2=9.99

print("{0:<30s} {1:6.2f}".format("Pythonfor DevOps",price1))
print("{0:<30s} {1:6.2f}".format("Pythonfor DevOps",price2))
print("_"*37)
print("{0:<30s} {1:6.2f}".format("Total",price1+price2))

#Formatted String Literal
print("\n"*2)

name="Vitaliy"
str=f"Hello {name}"
print(str)

calc=f"Ten by twenty is: {10*20}"
print(calc)







