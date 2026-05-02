"""
Datastructures: List

Use case: Lists are used to store multiple items / collection of items in a single variable
"""
from typing import List, TypedDict

# Create a list
fruits: List[str] = ["Apple", "Banana", "Cherry"]
print("Fruits:", fruits)
print("Type:", type(fruits),"\n")

numbers: List[int] = list(range(10))
print("Numbers:", numbers,)
print("Type:", type(numbers),"\n")

# Accessing to list items
first_fruit: str = fruits[0]
second_fruit: str = fruits[1]
last_fruit: str = fruits[-1]

print(f"First fruit: {first_fruit}\n"
      f"Second fruit: {second_fruit}\n"
      f"Last fruit: {last_fruit}\n")

first_number: int = numbers[0]
third_number: int = numbers[2]
last_number: int = numbers[len(numbers) - 1]

print(f"First number: {first_number}\n"
      f"Third number: {third_number}\n"
      f"Last number: {last_number}\n")

# Change list items
fruits[1] = "Pineapple"
print("New fruits:", fruits)

fruits[0:2] = ["Kiwi", "Watermelon", "Avocado"]
print("After change a range of fruits:", fruits)

# Insert items to a list
names: List[str] = []

while len(names) < 3:
    name: str = input('Enter a name: ')
    names.insert(0, name)

print("Names:", names)

# Add list items
while True:
    fruit: str = input("Add a fruit: ")
    
    if fruit:
        fruits.append(fruit)
    
    quit: str = input('Quit (yes/no)? ')
    if quit.lower() in ('yes', 'y'):
        break

print("New fruits:", fruits)

# Extend list

persons1: List[str] = ['Jack', 'Jean', 'John']
persons2: List[str] = ['Kouassi', 'Koffi', 'Konan', 'Kouamé']

persons1.extend(persons2)
persons: List[str] = persons1
print("Extended persons:", persons)

# Remove list items

employees: List[str] = ["Jack", "Jean", "John"]
employees.remove("John") 
print("Empoyees after removed 'John':", employees)

# Remove specified index
employees.pop(0)
print("Empoyees after removed item at 0 index:", employees)

# Clear the list
employees.clear()
print("Empty employees list:", employees)

# Loops through list
class Person(TypedDict):
    name: str
    age: int
    city: str
    job: str
    salary: float

def show_person_infos(person: Person):
    print(f"\nName:{person['name']}"
          f"\nSalary: ${person['salary']}"
          f"\nCity: ${person['city']}\n")

persons: List[Person] = [
    {
        "name": "Alice",
        "job": "Engineer",
        "salary": 3500.0,
        "age": 28,
        "city": "Abidjan"
    },
    {
        "name": "Michael",
        "job": "Teacher",
        "salary": 2200.0,
        "age": 35,
        "city": "Yamoussoukro"
    },
    {
        "name": "Sophia",
        "job": "Doctor",
        "salary": 5000.0,
        "age": 40,
        "city": "Bouaké"
    },
    {
        "name": "Daniel",
        "job": "Designer",
        "salary": 2700.0,
        "age": 26,
        "city": "San Pedro"
    },
    {
        "name": "Emma",
        "job": "Developer",
        "salary": 4200.0,
        "age": 31,
        "city": "Korhogo"
    }
]

for person in persons:
    show_person_infos(person)