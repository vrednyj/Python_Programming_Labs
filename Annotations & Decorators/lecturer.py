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

from random import randint
Lecturers_List = ["Pat", "Evelyn", "Priyank", "Bob", "Maria", "Ruth"]

class LECTURER:
    def __init__(self, name):
        self._lect_name = name

    @property
    def lnumber(self):
        """This is a getter function for lnumber"""
        return self._lnumber

    @property
    def lect_name(self):
        """The property (getter) must be created before a setter can be made"""
        return self._lect_name

    @lect_name.setter
    def lect_name(self, val):
        """restricting values to a predefined set"""
        print("Restrict")
        if val not in Lecturers_List:
            raise ValueError("Invalid lecturer")
        self._lect_name = val

    @lect_name.deleter
    def lect_name(self):
        """The deleter is called
        when del is called"""
        print("del called")
        del self._lect_name

    @staticmethod
    def random_lecturer():
        print (randint(0,3))
        return

#Lecturers_List[randint(0, 3)]



