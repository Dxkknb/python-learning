"""
A function is a block of code which only runs when it is called
"""

# Creating a function
def greet():
    print("Hi Mom")

# Return Values
def get_greeting(name: str):
    return f"Hi {name}"

print(get_greeting("John"))
print(get_greeting("Bernard"))

# Function Arguments
def withdraw_from_account(amount: float, bank_amount: float):
    if bank_amount >= amount:
        return True
    return False

amount = 1_200

if withdraw_from_account(amount, 16_000):
    print(f"You withdraw ${amount} from your bank account.")
    print(f"It remains ${16_000 - amount} on your account.")
else:
    print("The amount is too high!")

# Python *args and **kwargs

def multiply(*args):
    total = 1
    for num in args:
        total *= num
    
    return total

print(multiply(2,3, 4, 5, 6, 7))


def get_user(**kwargs):
    for key in kwargs:
        print(f"{key} => {kwargs[key]}")

get_user(id=1, name="John Doe", age=25, job="Civil Engineer")