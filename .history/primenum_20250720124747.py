num = 11

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is NOT a prime number (divisible by {i})")
            break
    else:
        print(f"{num} is a PRIME number")
else:
    print("Not a prime number")