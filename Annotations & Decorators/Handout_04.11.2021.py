# -------------------------------------------------------------------------------
# Name:        Handout_04.11.2021.py
# Project:     Python_Programming_Labs
#
# Author:      Vitaliy Baseckas
#
# Created:     04.11.2021
# Copyright:   (c) Vitaliy Baseckas 2021
# Licence:     <your licence>
# -------------------------------------------------------------------------------

def demo_generic_typet():
    ages: List[int] = [12, 22, 33]
    ages2 = [21, 32]  # type: List[int] # annotation for python 2.x legacy apps
    ages3 = [1, 0]
    ages.append("s")  # hover over "s" for hint
    ages2.append("s")  # no hint as type is not declared
    print(ages)
    print(ages2)
    ages.append([1, 2, 3])
    print(ages)
    ages3.append("k")
    print(ages3)


demo_generic_typet()


def data_in_series_examples():
    # In dictionaries the types of both the keys and values must be provided
    module_grade: Dict[str, float] = {'py_grade': 65.0, 'devops_grade': 71.0}
    module_grade[2] = "module name"  # this works but is not what you want

    # In tuples the types of all the elements are listed
    student_1: Tuple[int, str, float] = (30, "M. Doherty", 70.2)
    # adding extra items to the tuple, either in series or different does
    # not cause any issue
    student_2: Tuple[int, str, float] = (55, "A. Pearson", 99, 55)
    student_3: Tuple[str, str, str] = (55, "A. Pearson", 99, 55)
    print(student_1)
    print(student_2)
    print(student_3)


data_in_series_examples()


def type_aliases():
    lnum = str
    print(lnum)
    student_lnum: lnum = "L123456"
    print(lnum)
    print(student_lnum)
    student_lnum = 12
    print(student_lnum)
    lnum = 10
    print(lnum)
type_aliases()