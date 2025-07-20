num = 11

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not prime number", i)
        else:
            print("Prime number", i) 
else:
    print("Not Prime number")               