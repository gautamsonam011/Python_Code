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


# 1. Two Eggs Problem (Classic Logic)
# You are given two identical eggs and access to a 100-floor building. Eggs may break if dropped from a certain floor or above. You need to find the highest floor from which you can drop an egg without it breaking, using the fewest number of drops.

# How do you solve this with the minimum number of drops in the worst case?/

def two_eggs_problem(n_floors=100):
    # Find the optimal starting point (minimum drops)
    drops = 0
    while (drops * (drops + 1)) // 2 < n_floors:
        drops += 1

    attempts = 0
    current_floor = 0
    step = drops

    # Simulated function for whether the egg breaks
    # You can replace `target` with an actual unknown threshold
    target = 73  # Example: egg breaks at floor 73+

    # First egg
    while current_floor < n_floors:
        next_floor = current_floor + step
        attempts += 1
        print(f"Drop 1st egg from floor {next_floor}")
        if next_floor >= target:
            print(f"Egg broke at floor {next_floor}")
            break
        current_floor = next_floor
        step -= 1

    # Second egg
    for floor in range(current_floor + 1, next_floor):
        attempts += 1
        print(f"Drop 2nd egg from floor {floor}")
        if floor >= target:
            print(f"Egg broke at floor {floor}")
            return floor - 1, attempts

    return next_floor - 1, attempts

floor, total_attempts = two_eggs_problem()
print(f"Highest safe floor: {floor}")
print(f"Total attempts: {total_attempts}")


# 2. The Poison Bottle
# You have 1000 bottles of soda, and one is poisoned. The poison is lethal in exactly 24 hours. You have 10 test strips that will show if poison is present after 24 hours.

# How can you identify the poisoned bottle in 24 hours, using the fewest number of strips?
 
# Problem Facts:
# 1000 bottles, 1 is poisoned.

# 10 test strips.

# You get results in 24 hours, and can only test once.

# Poison is detectable even in tiny amounts.

# Number of bottles and test strips
num_bottles = 1000
num_strips = 10

# Let's assume bottle number 845 is poisoned (you can change this value)
poisoned_bottle = 805
print("Actual poisoned bottle:", poisoned_bottle)

# Initialize test strips: 0 = clean, 1 = shows poison
test_strips = [0] * num_strips

# Go through each bottle from 0 to 999
for bottle in range(num_bottles):
    if bottle == poisoned_bottle:
        # Convert bottle number to 10-bit binary
        binary = format(bottle, '010b')  # e.g., '1101001101' for 845

        # Apply drops to test strips based on binary representation
        for i in range(num_strips):
            if binary[num_strips - 1 - i] == '1':
                test_strips[i] = 1

# Reconstruct binary number from test strips after 24 hours
result_binary = ''
for i in range(num_strips - 1, -1, -1):
    result_binary += str(test_strips[i])

# Convert binary string to integer (bottle number)
detected_poisoned_bottle = int(result_binary, 2)

print("Detected poisoned bottle:", detected_poisoned_bottle)



