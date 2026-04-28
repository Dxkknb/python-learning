"""
Booleans represent one of two values: True or  False
"""

# Compare two values and evaluate the result
print(10 > 9)
print(10 == 9)
print(10 < 9)

# Run a condition in a if statement
number_1 = 200
number_2 = 153

if number_2 > number_1:
    print(f"{number_2} is greater than {number_1}")
else:
    print(f"{number_2} is not greater than {number_1}")

# Evaluate Values and Variables
print(bool("Hello"))
print(bool(15))
print(bool(["apple", "cherry", "banana"]))

# Some values are False
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool({}))
print(bool([]))

