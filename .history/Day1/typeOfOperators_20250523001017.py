# An operator is a symbol that performs a certain operation between operands 

# a + b               + operator a,b is operands

# (1) Arithmetic Operators (+, -, *, /, %, **, //)
a = 34
b = 25

sum = a+b
print(sum)

sub = a-b
print(sub)

mult = a*b
print(mult)

div = a/b
print(div)

mod = a%b
print(mod)

sq = a**b
print(sq)

floorDiv = a//b
print(floorDiv)

# (2) Relational operators (==, !=, >, <, >=, <=)

print("Equal to", a==b)
print("Not equal to", a != b)
print("Greater than", a > b)
print("Less than", a < b)
print("Greater than equal to", a >= b)
print("Less than equal to", a <= b)

# (3) Assignment Operators(=, +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=, :=)

# n1 = 20
# n2 += 20 n2 = n2+20

# (4) Logical operators (and, or, not)

print(a and b)
print( not False)
print(not b)
print(a or b)

x = 23

print( x > 20 and x < 24)
print(x > 20 or x < 35)
print(not x < 21)

# (5) Identity Operators (is, is not)

l1 = [23, 54, 67]
l2 = [32, 56, 23]

print(l1 is l2)
print(l1 is not l2)

# (6) Membership Operators (in, not in)

print(23 in l1)
print(45 not in l2)


