# -------------------------------------------------------------------------------
# Name:        Lab8_Q1.py
# Project:     Python_Programming_Labs
#
# Author:      Vitaliy Baseckas
#
# Created:     03.11.2021
# Copyright:   (c) Vitaliy Baseckas 2021
# Licence:     <your licence>
# -------------------------------------------------------------------------------
'''Create a person class. Create a class to represent students which inherits from the person class.
Each student should have defined functions which include ‘attendCollege’ and ‘sitExams’.
Create a lecturer class which inherits from the person class. The person class should include
methods ‘mark CA’ and ‘lecture’. Simply print a statement regarding the task (function) in each
instance. Consider what the person class might include that is common functionality.'''


class PERSON:
    def __init__(self,name,attendance,mark,lecture,exams):
        self.mark=mark
        self.lecture=lecture

    def print_the_mark(self):
        print("Student's mark: {}".format(self.mark))

    def print_lecture(self):
        print("Lecture: {}".format(self.lecture))


class STUDENT(PERSON):
    students_in_class=0
    def __init__(self, name,attendance,mark,lecture,exams):
        super().__init__(name,attendance,mark,lecture,exams)
        self.attendance=attendance
        self.exams=exams
        STUDENT.students_in_class+=1

    def print_attendColleg(self):
        print("Attendance:{}".format(self.attendance))

    def print_sitExams(self):
        print("Does he need to do exams: {}".format(self.exams))

class LECTURE(STUDENT):
    def __init__(self,name,attendance,mark,lecture,exams):
        super().__init__(name,attendance,mark,lecture,exams)
        self.name=name

    def print_hello(self):
        print('Hello from lecture class')

    def print_name(self):
        print("Student name: {}".format(self.name))

#name,attendance,mark,lecture,exams
student1=LECTURE("Michael Jackson","85%","F","OOPS","YES")
student1.print_name()
student1.print_lecture()
student1.print_the_mark()
student1.print_attendColleg()
student1.print_sitExams()
student1.print_hello()

student2=PERSON("Jimmy Morison","65%","B","DEVOPS","NO")
student2.print_lecture()
student2.print_the_mark()
setattr(student2,"attendance","65%")
print(getattr(student2,"attendance"))

student3=STUDENT("Donald Trump","100%","C","JAVA","YES")
setattr(student3,"name","Donald Trump")
print("Student's name: {}".format(getattr(student3,"name")))
student3.print_lecture()
student3.print_the_mark()
student3.print_attendColleg()
student3.print_sitExams()

print("Students in class:".format(STUDENT.students_in_class))

