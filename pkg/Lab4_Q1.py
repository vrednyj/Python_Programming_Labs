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


lnumbers=("L12345","L54321")
module_list=["Java_ooprogramming","Python_Scripting"]
java_grades={"L12345":40,"L54321":70}
python_grades={"L12345":69,"L54321":58}


for i in lnumbers:
        print("Student: {} Subject: {} Grade: {} Subject: {} Grade: {}".format(i,module_list[0],java_grades[i],module_list[1],python_grades[i]))
