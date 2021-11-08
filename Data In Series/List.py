# -------------------------------------------------------------------------------
# Name:        List.py
# Project:     Python_Programming_Labs
#
# Author:      Vitaliy Baseckas
#
# Created:     08.11.2021
# Copyright:   (c) Vitaliy Baseckas 2021
# Licence:     <your licence>
# -------------------------------------------------------------------------------
student1_details=[20,"Michael Jackson",77.5]
student2_details=[30,"Melerin Monro",65]

class_of_students=[student1_details,student2_details,"module title",[1,2,3]]
group_of_students =student1_details+student2_details

group_of_students = class_of_students[0:2] #this will copy the student1_details and student2_details part of our list
print(group_of_students)
print("1st student, 2nd datum is: {0}".format(group_of_students[0][1])) #accessing internal data is as before
second_group_of_students=student1_details+student2_details #joining two lists
print("{0} {1}".format("second_group_of_students",second_group_of_students))
third_group_of_students=[] # create an empty list
third_group_of_students+=second_group_of_students #add second group to existing contents of third group
print("Is Michael in list? {}".format(("Michael" in group_of_students[0][1])))
print("Is Michael in list? {}".format(("Michael" in group_of_students[0]))) #why is it different?
print ("{}".format(class_of_students[3][2]))

print("Third group of students {}".format(third_group_of_students))


grades=[1,2,3,4,5,9,5,3,8,7,6]
nu_grades=[grades]*2
print(nu_grades)
nu_grades[0][0]=6
print(nu_grades)
print(len(grades))
grades.sort()
print(grades)
grades.reverse()
print(grades)
grades.remove(2)
print(grades)
print(grades.count(6))
print(grades)
print(grades.pop(6)) #returns the element was removed
print(grades)


