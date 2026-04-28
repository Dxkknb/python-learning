"""
Exercises to practise conditions in python
"""

# Exercise 1: Even or Odd

number = int(input("Enter in integer: ").strip())

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

# Exercise 2: Age Category

age = int(input("How old are you? "))

if age >= 20:
    print("Adult")
elif age >= 13:
    print("Teenager")
elif age > 0:
    print("Child")
else:
    print("Not born")

# Exercise 3: Maximum of Three Numbers

def maximum(a: int, b: int, c: int) -> int:
   if a >= b and a >= c:
       return a
   elif b >= a and b >= c:
       return b
   return c

number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))
number3 = int(input("Number 3: "))

print(f"Maximum of {number1}, {number2}, {number3} is {maximum(number1, number2, number3)}")

# Exercise 4: Grade Evaluation

score = int(input("Provide the score (between 0 tà 100): "))
grade = ""

if 100 >= score >= 0:
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
else:
    print("the score must be between 0 and 100")

if grade:
    print(f"Score: {score}\nGrade: {grade}")

# Exercise 5: Simple Calculator

print("--------------------------- SIMPLE CALCULATOR ---------------------------")

num_1 = int(input('Enter the first number: '))
num_2 = int(input('Enter the second number: '))
operation = input("Choose an operation (+, -, x, /): ")

result = 0

if operation == "+":
    result = num_1 + num_2
elif operation == "-":
    result = num_1 - num_2
elif operation == "x":
    result = num_1 * num_2
elif operation == "/":
    if num_2 == 0:
        print("operation impossible")
    else:
        result = num_1 / num_2

if result:
    print(f"{num_1} {operation} {num_2} = {result}")
