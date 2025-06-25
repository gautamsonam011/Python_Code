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


