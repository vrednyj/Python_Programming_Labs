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

from lecturer import LECTURER
from person import PERSON

if __name__ == '__main__':

    Jay=PERSON("Jay Khan")
    Jay.display_person_details()
    Jay.name=("Jay Ray")
    Jay.display_person_details()

    Enid=PERSON("Enid")
    Enid.display_person_details()
    Enid.name = "Enid Blyton" # Function is called as if it were a property due to annotation
    Enid.display_person_details()

    lecturer1=LECTURER("Faraday") # instance can be created with any name

    try:
        lecturer1.lect_name = "Oops" # Can't use a name outside of the set list. Demo only.
    # set the name to one of predefined values
    except ValueError:
    # here the static method is called without an instance of the class
        print("Pick a valid name such as {}!".format(LECTURER.random_lecturer()))

    #LECTURER.random_lecturer()
    name_var = lecturer1.lect_name # get name using getter method
    print("Lecturer is: {}".format(name_var))

    del lecturer1.lect_name # delete variable not just the value of the variabl




