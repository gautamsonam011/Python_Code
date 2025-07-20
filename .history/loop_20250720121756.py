for i in range(11):
    print(i)

for i in range(0, 11, 2):
    print(i)  

for i in range(0, 50):
    if i % 2 == 0:
        print("Even number is", i)
    elif i % 2 != 0:
        print("Odd number is", i)  
    else:
        print("Not Even and no Odd")          

l = [65, 78, 43, "gfg", True]

print(len(l))

# slice 

sl = l[2]
print(sl)