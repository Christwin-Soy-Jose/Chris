import math
def isitvalidtriangle(side1,side2,side3):
    sides=[side1,side2,side3]
    sides.sort(reverse=True)
    print(sides)
    hypotenuse=sides[0]
    side1=sides[1]
    side2=sides[2]
    if hypotenuse==math.sqrt(side1**2+side2**2):
        print("its a right angled triangle")
    else:
        print("it is not a right angled triangle")
side1=int(input("enter the side1"))
side2=int(input("enter the side2"))
side3=int(input("enter the side3"))
isitvalidtriangle(side1,side2,side3)
