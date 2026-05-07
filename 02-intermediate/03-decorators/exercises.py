"""
Exercises using decorators
"""

import time


# TODO: Execution time logger
def measure_time(func):
    def inner(*args, **kwargs):
        t = time.time()
        func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - t}")
    return inner

@measure_time
def greeting(name):
    time.sleep(2)
    print(f"Hello {name}")

greeting("Konan Bernard")

# TODO: Function call Counter

def say_count(func):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"{func.__name__} has been called {count} time{'s' if count > 1 else None}")
        return func(*args, **kwargs)
    return inner

@say_count
def hello():
    print("hello")

hello()
hello()
hello()

# TODO: Login required message
logged_in = False

def login_required(func):
    def wrapper(*args, **kwargs):
        if not logged_in:
            print("Access denied. Please log in first.")
            return None
        return func(*args, **kwargs)
    return wrapper

@login_required
def dashboard():
    print("Welcome to your dashboard.")

@login_required
def profile():
    print("This is your profile page.")

# User is not logged in
dashboard()

print("User logs in ....")

# Simulate login
logged_in = not logged_in

dashboard()
profile()

# TODO: Fibonacci

def cache(func):
    stored_results = {}

    def wrapper(n):
        if n in stored_results:
            return stored_results[n]

        result = func(n)
        stored_results[n] = result

        return result

    return wrapper

@cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))
