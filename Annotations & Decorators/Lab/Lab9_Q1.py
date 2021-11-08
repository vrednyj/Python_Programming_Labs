# -------------------------------------------------------------------------------
# Name:        Lab9_Q1.py
# Project:     Python_Programming_Labs
#
# Author:      Vitaliy Baseckas
#
# Created:     04.11.2021
# Copyright:   (c) Vitaliy Baseckas 2021
# Licence:     <your licence>
# -------------------------------------------------------------------------------
'''Create a student class, module class, room class. Associate each appropriately. Annotate the
files appropriately. Use the Python documents included PEP 526 to decide on the most
appropriate annotations to use'''

class STUDENT:
    def __init__(self,name):
        self._name = name  # cannot be accessed outside of class

    @property
    def name(self):
        return self._name  # getter

    @name.setter
    def name(self, name):
        self._name = name  # cannot be accessed outside of class

    @name.getter
    def name(self):
        return self._name

    def display_person_details(self):
        print("Name: {}".format(self._name))


class MODULE:
    def __init__(self, module):
        self._module = module  # cannot be accessed outside of class

    @property
    def module(self):
        return self._module  # getter

    @module.setter
    def module(self, module):
        self._module = module  # cannot be accessed outside of class

    @module.getter
    def module(self):
        return self._module

    def display_module_details(self):
        print("Module: {}".format(self._module))

class ROOM:

    def __init__(self, room):
        self._room = room  # cannot be accessed outside of class

    @property
    def room(self):
        return self._room  # getter

    @room.setter
    def room(self, room):
        self._room = room  # cannot be accessed outside of class

    @room.getter
    def room(self):
        return self._room

    def display_module_details(self):
        print("Module: {}".format(self._room))

var1=STUDENT("Michael Jackson")
var1.display_person_details()
var1.name=("Jimmy Morrison")
var1.display_person_details()


var2=MODULE("OOPS")
var2.display_module_details()
