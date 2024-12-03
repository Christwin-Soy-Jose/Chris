def mult_numbers(n1,n2):
    if n2==1:
        return n1
    else:
        return n1+mult_numbers(n1,n2-1)
n1=int(input("enter the number"))
print(mult_numbers(n1,n2))
n2=int(input("enter the number"))