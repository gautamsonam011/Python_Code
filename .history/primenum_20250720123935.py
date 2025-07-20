num = 51

if num > 1:
    for i in (2, num):
        if num % i == 0:
            print("Not prime number", i)
        else:
            print("Prime number", i) 
else:
    print("Not prime number")               