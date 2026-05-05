"""
Python Sets
"""

# Create a set
fruits = {"Apple", "Cherry", "Avocado", "Banana", "Cherry", "Apple"}

print(fruits, type(fruits))

# Access Items: cannot access items in a set by referring to an index or a key
for fruit in fruits:
    print(fruit)

# Check if an item is in a set

if "Banana" in fruits:
    print("'banana' is in fruit's list")
else:
    print('Buy a \'banana\'')