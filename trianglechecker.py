import math
def isitvalidtriangle(hypotenuse,base,perpendicular):
    if hypotenuse==math.sqrt(base**2+perpendicular**2):
        print("its a right angled triangle")
    else:
        print("it is not a right angled triangle")
hypotenuse=int(input("enter the hypotenuse"))
base=int(input("enter the base"))
perpendicular=int(input("enter the perpendicular"))
isitvalidtriangle(hypotenuse,base,perpendicular)
