
def add_numbers(n1,n2):
    if n2==0:
        return n1
    else:
        return add_numbers(n1+1,n2-1)
n1=int(input("enter the 1st number"))
n2=int(input("enter the 2nd number"))
print(add_numbers(n1,n2))