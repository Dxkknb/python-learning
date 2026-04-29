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

# Exercise 6: Advanced Discount System
import datetime

purchase_amount = float(input("Provide the purchase amount: "))
customer_type = input("Precise the customer type (regular, member, VIP): ").strip()

today = datetime.datetime.today().weekday()

if customer_type == "member":
    if purchase_amount >= 100_000:
        purchase_amount -= purchase_amount * 0.15
    elif purchase_amount >= 50_000:
        purchase_amount -= purchase_amount * 0.1
elif customer_type == "VIP":
    if purchase_amount >= 100_000:
        purchase_amount -= purchase_amount * 0.2
    elif purchase_amount >= 50_000:
        purchase_amount -= purchase_amount * 0.3

if today >= 5:
    purchase_amount -= purchase_amount * 0.05

print("------------------------- PURCHASE INVOICE ------------------")
print(f"purchase amount: ${purchase_amount}")
print(f"Customer type: {customer_type}")

# Exercise 7: Tax Calculation System

salary = float(input("Provide the salary: "))
married = input("Are you married ? (Yes/No) ")
number_of_children = int(input("How many children do you have? "))
tax = 0

if 100_001 <= salary <= 300_000:
    tax = 0.1
elif 300_001 <= salary <= 700_000:
    tax = 0.2
elif salary  >= 700_001:
    tax = 0.3

if married.lower() == "yes" and tax:
    tax -= 0.05

if number_of_children >= 3 and tax:
    tax -= 0.1

remained_salary = salary - tax * salary

print(f"Remained salary: ${remained_salary}")

# Exercise 8: Login System with Attempts
correct_credentials = {
    "username": "Alice",
    "password": "12345"
}
print("------------------- LOGIN SYSTEM -------------------")

total_attempts = 0

while total_attempts < 3:
    username = input("Username: ")
    password = input("Paswword: ")
    
    total_attempts += 1

    if (username == correct_credentials['username'] and password == correct_credentials['password']):
        print("Access granted")
        break
    else:
        if total_attempts == 3:
            print("Account locked")
        else:
            print("Username or password is wrong.")
            print(f"{3 - total_attempts} attempts left")