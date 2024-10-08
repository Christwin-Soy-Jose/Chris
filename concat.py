'''
Author:Christwin Soy Jose
Date;08/10/2024
program to accept 1st and last name and concatenate it and extract the last name alone
'''

_1stname=input("enter the 1st name")
lastname=input("enter the last name")
fullname=_1stname+" "+lastname
num=len(_1stname)
print(fullname)
print(fullname[num+1:])