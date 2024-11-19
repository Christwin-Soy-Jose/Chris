num=int(input("enter the number"))
for number in range(1,num):
    for number2 in range(num-number):
        print(" ",end="")
    for number3 in range(1,2*number):
        print("*",end="")
    print()