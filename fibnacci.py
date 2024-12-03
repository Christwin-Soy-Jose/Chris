def fibonacci(n):
    sequence=[]
    number_1,number_2=0,1
    for i in range(n):
        sequence.append(number_1)
        number_1,number_2=number_2,number_1+number_2
    return sequence
print(fibonacci(10))