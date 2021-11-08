# -------------------------------------------------------------------------------
# Name:        Copying Lists.py
# Project:     Python_Programming_Labs
#
# Author:      Vitaliy Baseckas
#
# Created:     08.11.2021
# Copyright:   (c) Vitaliy Baseckas 2021
# Licence:     <your licence>
# -------------------------------------------------------------------------------
import copy

student1_details=[20,"Michael Jackson",77.5]
student2_details=[30,"Melerin Monro",65]

student3_details=student2_details
print("Student 2 details {}".format(student2_details))
print("Student 3 details {}".format(student3_details))

student3_details[0]=44
print("After Change:")
print("Student 2 details {0}, with id of {1}".format(student2_details,id(student2_details)))
print("Student 3 details {0}, with id of {1}".format(student3_details,id(student3_details)))


#student2_details = [ 21, "Mairead Hannigan", 67]
student3_details = student2_details[:] # this works but is not great
student4_details = copy.deepcopy(student2_details)
student5_details = copy.deepcopy(student4_details)
student3_details[0]=15
student4_details[0]=999
student5_details[0]=88
print("-"*10)
print("Student 2 details {0}, with id of {1}".format(student2_details,id(student2_details)))
print("Student 3 details {0}, with id of {1}".format(student3_details,id(student3_details)))
print("Student 4 details {0}, with id of {1}".format(student4_details,id(student4_details)))
print("Student 5 details {0}, with id of {1}".format(student5_details,id(student5_details)))