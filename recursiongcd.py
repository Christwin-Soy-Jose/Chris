def gcd(n1,n2):
    if n1%n2==0:
        return n2
    else:
        return gcd(n2,n1%n2)
n1=int(input("enter the number 1"))
n2 =int(input("enter the number 2"))

print(gcd(n1,n2))