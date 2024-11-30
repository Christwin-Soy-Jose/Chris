def phone(number):
    if len(number)==10 and number[0] in "789":
        print("its a number")
    else:
        print("not a number")
number=input("enter the number")
phone(number)