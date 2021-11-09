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
Investigate, using examples, the use of @callable, @collection and @overload.

'''
from room_1 import ROOM
from student_1 import STUDENT
from module_1 import MODULE


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

module1: classmethod
module1=MODULE("Software Eng")
module1.display_room_details()
print(callable(module1.__call__))
print(MODULE)

