"""
Python Decorators
Add functionality to an existing function with decorators
"""

# TODO: Function are objects
def hello():
    print("Hello")

greeting = hello # Even functions are objects
greeting() # Call the new function

# TODO: How Python Decorators work
def hello(func):
    def wrapper():
        print("Hello ", end="")
        func()
    return wrapper

def get_name():
    print("Alice")

obj = hello(get_name)
obj()

# Syntactic sugar
def display(func):
    def inner():
        print("The current user is: ", end="")
        func()
    return inner

@display
def who():
    print("Konan")

who()

def display_sum(func):
    def wrapper(a, b):
        print(f"{a} + {b} = ", end="")
        return func(a, b)
    return wrapper

@display_sum
def sum_ab(a, b):
    print(a+b)

sum_ab(5, 6)

# Real world examples
# TODO: Time execution

import time

def time_exec(func):
    def inner(*args):
        t = time.time()
        res = func(*args)
        print(f"the function {func.__name__} took {time.time() - t} seconds to run")
        return res
    return inner

@time_exec
def greet(name):
    time.sleep(2)
    print("Hello " + name)

greet("Konan")
