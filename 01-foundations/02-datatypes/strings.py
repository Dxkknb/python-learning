"""
Strings in python are surrounded by either single quotation marks, or double quotation marks.
"""

name = "Konan Koffi"
animal = 'Dog'

print("Name:", name)
print("Animal:", animal)

# Strings are Arrays of unicode characters
brand = "Coca Cola"

print(f"First character: {brand[0]}")
print(f'Third character: {brand[2]}')
print(f"Last character: {brand[-1]}")

# Looping through a string
fruit = "Pineapple"

for character in fruit:
    print(character)

# Length of a string
greeting = "Hello everyone!"
print(greeting, f", length: {len(greeting)}")
