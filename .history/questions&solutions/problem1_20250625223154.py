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
poisoned_bottle = 845
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


# 3. Bridge Crossing Puzzle
# Four people need to cross a bridge at night. They have one flashlight and the bridge can hold only two people at a time. The crossing times are:

# Person A: 1 minute

# Person B: 2 minutes

# Person C: 5 minutes

# Person D: 10 minutes

# Whenever two people cross, they must go at the slower person’s pace, and the flashlight must be carried.

# What is the minimum total time for all four to cross?

A = 1
B = 2
C = 5
D = 10

total_time = 0

# A and B  cross 

total_time += B
print("A and B cross time", B)
# Return A 

total_time += A
print("A return time", A)

total_time += D

print("C and D cross time", D)

total_time += B

print("B return time", B)

total_time += B

print("A and B again cross", B)

print("Minimum total time", total_time)

# 4. Locker Riddle
# There are 100 lockers in a row, all initially closed. One person walks by and toggles every locker (open it if it’s closed, close it if it’s open). A second person toggles every second locker. A third toggles every third locker, and so on, up to the 100th person.

# After all 100 people have walked by, how many lockers are open, and which ones?

open_lockers = []

for i in range(1, 101):
    if int(i**0.5)**2 == i:
        open_lockers.append(i)

print("Open lockers:", open_lockers)
print("Total open lockers:", len(open_lockers))

# 5. Three Light Bulbs
# You are in a room with three switches, each corresponding to one of three light bulbs in another room. Once you leave the room to check the bulbs, you cannot return to the switch room.

# How can you determine which switch controls which bulb?

# 6. Water Jug Problem
# You have a 5-liter jug and a 3-liter jug, and access to unlimited water.

# How can you measure exactly 4 liters?

# 7. Coin Flip Puzzle
# You have 100 coins on a table, with exactly 10 coins showing heads, but you cannot see them. You are allowed to split them into two groups and flip any coins in either group.

# How do you split and flip to ensure each group has the same number of heads?




