# -------------------------------------------------------------------------------
# Name:        Lab4_Q1.py
# Project:     Python_Programming_Labs
#
# Author:      Vitaliy Baseckas
#
# Created:     09.10.2021
# Copyright:   (c) Vitaliy Baseckas 2021
# Licence:     <your licence>
# -------------------------------------------------------------------------------
'''Create a tuple of 2 fake student lnumbers. Create a list of 2 modules_subjects names that the
student takes. For each of the subjects create a dictionary with the student lnumber and the
grade for that module. See below tables for sample data.
Modify the code to read in a student Lnumber and using a combination of the above fields print
the name of the modules they take and the grade they received in each module.'''


lnumbers=("L12345","L54321")# tupple
module_list=["Java_ooprogramming","Python_Scripting"]# list
java_grades={"L12345":40,"L54321":70} #dictionary
python_grades={"L12345":69,"L54321":58} # dictionary


for i in lnumbers:# iteration by student numbers
        print ("Student: {} Subject: {} Grade: {} Subject: {} Grade: {}".format(i,module_list[0],java_grades[i],module_list[1], python_grades[i]))

# Asks to enter the student ln number
#print(lnumbers.index("L54321"))
while 1:
        student_input=input("Please enter a student ln number:")
        student_input=("{}".format(student_input.capitalize()))# in case l is small in the string. No checks of entered values performed here.
        if student_input not in lnumbers: # check if such student exists in DB
                print("{}".format('No such student in DB. Try again.'))
                pass
        else:
                print("Student name: {0} "
                      "|Subject 1: {1} ->Grade: {2} |Subject 2:{3} ->Grade:{4}".format(student_input,
                                            module_list[0],#java
                                            java_grades[student_input], #Grades from java dict
                                            module_list[1],#Python
                                            python_grades[student_input]))#Grades from python dict
                break



