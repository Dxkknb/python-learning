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

# Update item in tuple
fruits_list = list(fruits)
fruits_list[0] = "Avocado"
fruits_list = tuple(fruits_list)
print("New fruits:", fruits_list)

# Add items to a tuple
def add_item(items, item) -> tuple:
    items_list = list(items)
    items_list.append(item)
    return tuple(items_list)

fruit = input('Add a fruit:')

if fruit:
    fruits = add_item(fruits, fruit)
    print("New fruits:", fruits)

# Remove items
def remove_item(items: tuple, item) -> tuple:
    items_list = list(items)

    if item in items_list:
        items_list.remove(item)
        print(f"'{item}' removed with success")
    else:
        print(f"'{item}' not in collection")
    
    return tuple(items_list)

removed_fruit = input("Name of fruit to remove: ")
print(remove_item(fruits, removed_fruit))

# Unpack a tuple
names = ("Maria", "Julie", "Anne")
(maria, julie, anne) = names
print(maria, julie, anne)

# use asterisk
apple, *other_fruits, mango = fruits[:]

print("apple => ", apple)
print("other fruits =>", other_fruits)
print("mango =>", mango)

# Loop through a tuple

for name in names:
    print(name)

for i in range(len(names)):
    cur_name = names[i]
    print(f"{i} => {cur_name}")