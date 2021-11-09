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
'''
 Create a student class, module class, room class. Associate each appropriately. Annotate the
files appropriately. Use the Python documents included PEP 526 to decide on the most
appropriate annotations to use

'''
from room import ROOM
from student import STUDENT
from module import MODULE


def main():
    pass

if __name__ == '__main__':
    main()


student1: classmethod

student1=STUDENT("Michael Jackson")
student1.display_room_details()

room1: classmethod
room1=ROOM("IT LAB")
room1.display_room_details()

ROOM.room=("Chemistry LAB")
ROOM.display_room_details()

module1: classmethod
module1=MODULE("Software Eng")
module1.display_room_details()
