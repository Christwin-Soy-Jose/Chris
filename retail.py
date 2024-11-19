inventory=[("laptop",10,20000),("phone",55,9000),("bag",100,250),("charger",100,150)]
largest=0
for item in inventory:
    itemname,quantity,price=item
    stock=price*quantity
    print(itemname,"total value:",stock)
    if stock>largest:
        largest=stock
print(largest)