"""
Exercises using loops in python
"""

# Exercise 1: Print Numbers

for x in range(1, 11):
    print(x)

# Exercise 2: Sum of First Numbers

number = int(input("Provide a number: "))

if number < 1:
    print("The number must be greater than 1")
else:
    sum_of_nums = 0
    
    for i in range(number+1):
        sum_of_nums += i

    print(f"Sum of numbers from 1 to {number} = {sum_of_nums}")

# Exercise 3: Even Numbers in Range

for i in range(51):
    if i % 2 == 0:
        print(i)

# Exercise 4: Multiplication Table

number = int(input("provide a number: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# Exercise 5: Factorial calculator

print("------------------ FACTORIAL --------------------")
n = int(input("Provide a number: "))
factorial = 1

while n > 1:
    factorial *= n
    n -= 1

print(f"{number}! = {factorial}")
