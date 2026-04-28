"""
If else statement: Condition making
"""

# Basic decision
age = 20

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Multiple conditions
score = 75

if score >= 90:
    print("Grade: A")
elif score >= 75:
    print("Grade: B")
elif score >= 60:
    print("Grade: C")
else:
    print("Grade: F")

# Combined conditions

username = "alice"
password = "1234"

if username == "alice" and password == "1234":
    print("Access granted")
else:
    print("Wrong credentials")