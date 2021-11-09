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

class ROOM:
    def __init__(self, room):
        self._room = room # cannot be accessed outside of class

    @property
    def room(self):
        return self._room  # getter

    @room.setter
    def room(self, room):
        self._room  = room # cannot be accessed outside of class

    @room.getter
    def room(self):
        return self._room

    def display_room_details(self):
        print("Room: {}".format(self._room))




