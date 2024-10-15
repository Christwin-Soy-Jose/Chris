n=int(input("enter the number of students"))
btotal=0
gtotal=0
gh=0
bh=0
for i in range(n):
    gender=input("enter the gender")
    height=int(input("enter the height"))
    if gender in "maleMale":
        btotal+=1
        bh+=height
    elif gender in "Femalefemale":
        gtotal+=1
        gh+=height
print("avg height of boys is ",bh/btotal)
print("avg height of girls is ",gh/gtotal)
