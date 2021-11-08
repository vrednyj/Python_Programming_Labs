# -------------------------------------------------------------------------------
# Name:        Variables.py
# Project:     Python_Programming_Labs
#
# Author:      Vitaliy Baseckas
#
# Created:     08.11.2021
# Copyright:   (c) Vitaliy Baseckas 2021
# Licence:     <your licence>
# -------------------------------------------------------------------------------
print ("Student {0}, Age {1}".format(123456,21))
print ("Student {0:7d}, Age {1}".format(123456,21)) #add leading zeros
print ("Student {0:>10d}, Age {1}".format(123456,21)) # right align
print ("Student {0:<10d}, Age {1}".format(123456,21)) # left align
print ("Student {0:^10d}, Age {1}".format(123456,21)) #center
print ("Footballer Wages {:9,.2f} euros".format(1234567))
print ("Footballer Wages {:6,d} euros".format(1234567))
print("\n"*2) #two new lines


choice='a'
str = "This is a long string with nothing to say."
paragraph='''This is a very long string which can run over multiple lines if desired and can still
contain single ‘ or double “ quotes within it '''

print("{0}  {1} : {2}".format("str[0]"," prints the first letter in the string",str[0]))   #prints the first letter in the string
print("{0}  {1} : {2}".format("str[3:8]"," prints from ides 3 to 8",str[3:8])) #prints from ides 3 to 8
print("{0}  {1} : {2}".format("str[8:]"," prints from index 8 to the end",str[8:]))  #prints from index 8 to the end
print("{0}  {1} : {2}".format("str[-1]"," prints the last character in the string",str[-1]))
print("{0}  {1} : {2}".format("str[-2]"," prints the second last character in the string",str[-2]))
print("{0}  {1} : {2}".format("len(str)"," prints the length of the string",len(str)))

student_name="Paddy Dohertty"
student_name="Paddy Doherty"

studentA_grade=77
studentB_grade=77
studentC_grade=[77]
studentD_grade=[77]

print(studentA_grade is studentB_grade) #True
print(studentA_grade == studentB_grade) #True
print(studentC_grade == studentB_grade) #False
print(studentC_grade == studentD_grade) #True
print("\n"*2)
print(45+5.2)
print(45-5.2)
print(45*5.2)
print(45/5.2)
print(45//5.2)
print(45**5.2)
print(45%5.2)