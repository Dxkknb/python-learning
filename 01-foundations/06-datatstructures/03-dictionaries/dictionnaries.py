"""
Python Dictionnaries
"""

# Create a dictionnary
person = {
    "name": "Alice",
    "age": 25,
    "job": "Engineer",
    "salary": 3500.50,
    "city": "Abidjan"
}

print(person, type(person))

# Access items -> Error is key not exists
name = person["name"]
age = person["age"]
job = person["job"]
salary = person["salary"]
city = person["city"]

print(f"""
Name: {name}
Age: {age} years old
Job: {job}
Salary: ${salary}
""")

name_2 = person.get("model")
if name_2 is None:
    print("No 'model' in person data")
else:
    print('New name:', name_2)