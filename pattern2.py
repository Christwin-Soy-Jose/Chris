num=int(input("enter the number"))
for number in range(num):
    for number2 in range(num-number):
        print("*",end="")
    print()