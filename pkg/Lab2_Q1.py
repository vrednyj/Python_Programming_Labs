python_mission='''The mission of the Python Software Foundation is to promote, protect,
and advance the Python programming language, and to support and facilitate
the growth of a diverse and international community of Python programmers'''

print(python_mission.lower().count("s")) #Count the number of appearances of the letter s
#-> 7
print(python_mission.find("Python",25)) #Find the second instance of the word Python which occurs somewhere after position 25.
#-> 86
print("The word returned is: {}".format(python_mission[25:34]))
#-> The word returned is:  Software
print(python_mission.find("diverse"))
#-> 161
print("1234".isdigit())
#-> True
print(r"C:\users\ndarby\python3\python-3.5.1\bin")
#-> C:\users\ndarby\python3\python-3.5.1\bin
