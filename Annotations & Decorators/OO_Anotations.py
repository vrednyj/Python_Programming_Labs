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


def demo_generic_typet():
     ages:List[int] = [12, 22, 33]
     ages2 = [21, 32] # type: List[int] # annotation for python 2.x legacy apps
     ages.append("s") # hover over "s" for hint
     ages2.append("s") # no hint as type is not declared
     return ages, ages2


#def product_descriptor (item_name: str, id: int = 0) -> str:
def product_descriptor (item_name: str, ind: int = 0) -> str:
    print(id(item_name))
    print(id(ind))

    if ind == 10:
        return "Some description…"



if __name__ == '__main__':

    #Type Hints for Variables

    '''built in types'''
    age: int = 21
    grade: float = 77.5
    valid_reg: bool = True
    l_num: str = "L0012345"
    pwd_to_encrypt: bytes = b"5i77yP3d"

    print(age)
    print(grade)
    print(valid_reg)
    print(l_num)
    print(pwd_to_encrypt)

    age = "21"
    grade = "77.5"
    valid_reg = "False"
    l_num = 123456
    pwd_to_encrypt = "5i77yP3d"

    print(age)
    print(grade)
    print(valid_reg)
    print(l_num)
    print(pwd_to_encrypt)


    ages, ages2=demo_generic_typet()
    print(ages, ages2 )


    answer = product_descriptor("Hi",10)
    print(answer)









