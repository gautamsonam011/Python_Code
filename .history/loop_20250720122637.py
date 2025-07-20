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

# mutable 

l[0] = 356

print(l)

l[3] = 500
print(l)

l[0:3] = [50, 70, 90, 89]
print(l)

sum = 0

for i in l:
    sum = sum+i
    print(sum)
print(sum) 

# Maximun of number in list 
k = 0
for i in l:
    if i > k:
        k = i

        print("max", k)
