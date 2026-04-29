"""
A for loop is used for iterating over a sequence (list, tuple, dictionary, set, string)
"""

# For loop statement

fruits: list[str] = ["apple", "banana", "cherry"]

print("---------------- LIST OF FRUITS ----------------")

for fruit in fruits:
    print(" => ",fruit)

# Looping through a String

for index, character in enumerate("apple"):
    print(f"{index} => {character}")

# Break Statement

persons: list[str] = ["Alice", "Jean", "Marc", "Bernard"]

for person in persons:
    print(person)
    if person == 'Marc':
        break

# The Continue Statement

numbers = [x for x in range(0, 10)]

print("---------------- Even Numbers ----------------")

for number in numbers:
    if number % 2 == 1:
        continue
    print(number)

# The range() function

for x in range(0, 100, 10):
    if x % 5 == 0:
        print("=> ", x)

# Else in For Loop

nums = []

for x in range(1, 20):
    if x % 3 == 0:
        nums.append(x ** 2)
else:
    print("Final numbers: ", nums)

# Nested Loops
for row in range(1, 4):
    for col in range(0, 3):
        print(1, end = " ")
    print("\n")
