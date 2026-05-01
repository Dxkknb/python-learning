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

# Exercise 6: Reverse a number

integer = int(input('Enter an integer: '))

if integer < 0:
    print("Please, provide a positive integer.")
elif integer < 10:
    print(f"{integer} => {integer}")
else:
    integer_to_str = str(integer)
    reversed_str = ""
    
    for i in range(1, len(integer_to_str) + 1):
        reversed_str += integer_to_str[-i]

    print(f"{integer} => {reversed_str}")

# Exercise 7: Count Each Digits

number = int(input("Enter a number: "))

number_str = str(number)
digits = {}

for char in number_str:
    if char not in digits:
        digits[char] = 1
    else:
        digits[char] += 1

print(f"In {number_str}, they are:")
for digit in digits:
    if digits[digit] > 1:
        print(f"{digit} => {digits[digit]} times")
    else:
        print(f"{digit} => {digits[digit]} time")

# Exercise 8: Prime number Checker
number = int(input("Enter a number: "))

if number <= 1:
    print("Enter a number greater at least than 2")
elif number == 2:
    print(f"{2} is a prime number.")
else:
    is_prime = True

    # Check if number has others dividers over than 1 and number himself 
    for divider in range(2, number):
        if number % divider == 0:
            is_prime = False
            break
    
    if is_prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")

# Exercise 9: Pattern Printing
number = int(input("Enter a base of pyramid: "))

for i in range(1, number + 1):
    print("*" * i)

print()

for i in range(0, number):
    print("*" * (number - i))

print()

for i in range(1, number + 1):
    # Print spaces
    for j in range(number - i):
        print(" ", end="")
    
    # Print stars
    for k in range(2 * i - 1):
        print("*", end="")
    
    # Move to next line
    print()

# Exercise 10: Number Guessing Game
from random import choice

guessed_number = choice(range(1, 30))
ATTEMPTS = 5

user_stats = {
    "points": 0, # if win => 10pts, 0 if lost
    "attempts": 0
}

while user_stats["attempts"] < ATTEMPTS:
    user_number = int(input("Guess the mistery number: "))
    user_stats["attempts"] += 1

    if user_number == guessed_number:
        print("You guess the mistery number.")
        user_stats["points"] += 10
        break
    elif user_number < guessed_number:
        print("Too low")
    else:
        print("Too high")
    
    if user_stats["attempts"] < ATTEMPTS:
        print(f"You have {ATTEMPTS - user_stats['attempts']} chances left.")
        

print("End of guessing game.")
print("See your score below:")

print("----------- SCORE OF GUESSING GAME ------------")
print(f"Total attempts: {user_stats['attempts']}")
print(f"Total points won: {user_stats['points']}")