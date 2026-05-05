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

# Get dictionnary keys and values 
keys = person.keys()

for k in keys:
    print(f"{k} => {person[k]}") 

values = person.values()
print(values)

items = person.items()

for k, v in items:
    if k == "salary":
        print(f"{k}: ${v}")
    else:
        print(f"{k}: ${v}")

# Set a dictionary
person['city'] = "Yamoussoukro"
print("City updated:", person)