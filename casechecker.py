def checkcase(str1):
    uppercount=0
    lowercount=0
    for i in str1:
        if i.isupper():
            uppercount+=1
        elif i.islower():
            lowercount+=1
    print("lower count is", lowercount)
    print("uppercount is", uppercount)

text=input("enter the string")
checkcase(text)
