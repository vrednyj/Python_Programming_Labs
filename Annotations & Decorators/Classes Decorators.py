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

     def name(self):
        return self._name

     def display_person_details(self):
        print("Name: ".format(self._name))

class PERSON_1:

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


if __name__ == '__main__':

    Joe=PERSON("Joe Bloggs")
    Joe.display_person_details() #None

    Joe=PERSON_1("Joe Bloggs")
    Joe.display_person_details() #Joe Bloggs