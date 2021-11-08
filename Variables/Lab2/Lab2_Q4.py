# -------------------------------------------------------------------------------
# Name:        Lab2_Q4.py
# Project:     Python_Programming_Labs
#
# Author:      Vitaliy Baseckas
#
# Created:     09.10.2021
# Copyright:   (c) Vitaliy Baseckas 2021
# Licence:     <your licence>
# -------------------------------------------------------------------------------
'''
Question 4:Assume that the following is a single line taken from a *Nix password file. Separate out each field into
the appropriate variables using the slice operator [].
rlennon:x:1234:1001:Ruth Lennon:/users/rlennon:/bin/bash
Repeat the process using the split method.'''

string=r"rlennon:x:1234:1001:Ruth Lennon:/users/rlennon:/bin/bash"

user_login=string[0:7]
user_type=string[8:9]
password=string[10:14]
permission=string[15:19]
user_name=string[20:31]
user_dir=string[32:46]
user_shell=string[47:56]

# Manipulating string. Cutting to required peaces.
print("Login: {}".format(user_login))
print("User type: {}".format(user_type))
print("Password: {}".format(password))
print("Permission: {}".format(permission))
print("User name: {}".format(user_name))
print("User Dir: {}".format(user_dir))
print("Working shell: {}".format(user_shell))

#spliting string by ":" and coverting it into the list. The using the list elements below.
string=string.split(":")
print("\n{:*^50}\n".format("Another method"))
print("Login: {}".format(string[0]))
print("User type: {}".format(string[1]))
print("Password: {}".format(string[2]))
print("Permission: {}".format(string[3]))
print("User name: {}".format(string[4]))
print("User Dir: {}".format(string[5]))
print("Working shell: {}".format(string[6]))