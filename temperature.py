temp=int(input('enter the temp'))
ask=input("Is this in (C)elsius or (F)ahrenheit?")
if ask=='C':
    f=(9/5*temp)+32
    print(temp,"celsius is",f,'fahrenheit')
else:
    c=(5/9)*(temp-32)
    print(temp,'fahrenheit is',c,'celsius')