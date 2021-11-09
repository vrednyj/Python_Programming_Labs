#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      vbaseckas
#
# Created:     09/11/2021
# Copyright:   (c) vbaseckas 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class STUDENT:
    def __init__(self, student: str):
        self._student = student # cannot be accessed outside of class

    @property
    def student(self):
        return self._student  # getter

    @student.setter
    def student(self, student: str):
        self._student  = student # cannot be accessed outside of class

    @student.getter
    def student(self):
        return self._student

    def display_room_details(self):
        print("Student name: {}".format(self._student))