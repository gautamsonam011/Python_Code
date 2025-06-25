arr  = [32, 56, 78, -97, -3]

# for i in range(len(arr)):
#     if i < 0:
#         print(i)
a = []

# for i in arr:
#     if i < 0:
#         print(i)
#         a.append(i) 
# print(a)  

for i in arr:
    if i < 0:
        a.append(i)
print(len(a))   

for i in arr:
    if i == 78:
        i = i+1
        print(i)

