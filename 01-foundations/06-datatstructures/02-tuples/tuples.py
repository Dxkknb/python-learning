"""
Data structures: Tuples
A tuple is a collection which is ordered and unchangeable.
"""

# Create a tuple
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

print("fruits:", fruits)
print("Type:", type(fruits))

name = ('Konan',) # Tuple with one item

print(name, type(name))

# Access Tuple Items
first_fruit = fruits[0]
last_fruit = fruits[-1]

print("First fruit:", first_fruit)
print("Last fruit:", last_fruit)

# Range of indexes
four_fruits = fruits[:4]
print("Four fruits:", four_fruits)
print("from cherry to the end:", fruits[2:])

# Check if item exists
if "apple" in fruits:
    print("Yes, 'apple' is in the fruits tuple")
else:
    print("No 'apple' in the fruits tuple")