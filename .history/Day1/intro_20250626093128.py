print("Hello World!")
# Python is a case sensitive language . It means s, S both are different character
# Variable is a name given to a memory location in a program 

name = "Ice Cream"
age = 34
price = 34.56

print("product name is", name)

# 3 = 45
# print(3) this is not valid

# 34v = 78
# print(34v) invalid variable

print(type(name))
print(type(age))
print(type(price))

num1 = 100
num2 = 200

sum = num1+num2 
print(sum)

# comments

"""
multi-line
comment

"""
l = ["hello", 2, 4, 5]

print(len(l))

# What will be the output of the following Python code?
i = 1
while True:
    if i%3 == 0:
        break
    print(i)
    i += 1