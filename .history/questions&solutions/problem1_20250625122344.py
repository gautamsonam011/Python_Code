arr  = [32, 56, 78, -97, -3]

# for i in range(len(arr)):
#     if i < 0:
#         print(i)
a = []

for i in arr:
    if i < 0:
        print(i)
        x = a.append(i) 
print(x)      