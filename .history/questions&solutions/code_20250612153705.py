# Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

# Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case

def bit_count(n):
    # return bin(n).count('1')
    return bin(n)

# print(bit_count(1234))
print(bit_count(1234))

arr = [3, 5, 7, 8, 3]

for i in range(len(arr)):
    unique = True
    for j in range(len(arr)):
        if i != j and arr[i] == arr[j]:
            unique = False
            break
    if not unique:
        print("Duplicate item:", arr[i])



arr = [2, 4, 5, 4]
duplicates = []

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] == arr[j] and arr[i] not in duplicates:
            duplicates.append(arr[i])

# Print duplicate items
print("Duplicate items in the array:")
for item in duplicates:
    print("Item", item, "is duplicated")

s = "jhdskhsads"
counted = []
for i in range(len(s)):
    if s[i] not in counted:
        count = 1
    for j in range(i+1, len(s)):
        if s[i] == s[j]:
            count += 1

    if count > 1:
        print(s[i], "appears", count, "times")
    counted.append(s[i])

count = 0

for i in range(len(s)):
    if s[i] == 's':
        count += 1

print("'s' appears", count, "times")
