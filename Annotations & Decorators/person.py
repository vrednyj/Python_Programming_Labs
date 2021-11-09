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

class PERSON:

    def __init__(self, name):
        self._name = name # cannot be accessed outside of class

    @property
    def name(self):
        return self._name # getter

    @name.setter
    def name(self, name):
        self._name = name # cannot be accessed outside of class

    @name.getter
    def name(self):
        return self._name

    def display_person_details(self):
        print("Name: {}".format(self._name))