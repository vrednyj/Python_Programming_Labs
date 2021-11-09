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

class MODULE:
    def __init__(self, module: str):
        self._module = module # cannot be accessed outside of class

    @property
    def module(self):
        return self._module  # getter

    @module.setter
    def module(self, module: str):
        self._module  = module # cannot be accessed outside of class

    @module.getter
    def module(self):
        return self._module

    def display_room_details(self):
        print("Module: {}".format(self._module))