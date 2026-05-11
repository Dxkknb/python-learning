"""
Object Oriented Programming
"""

# Represent Employee

class Employee:

    def __init__(self, first: str, last: str, pay: float) -> None:
        self.first = first
        self.last = last
        self.email = f"{self.first}.{last}@company.com"
        self.pay = pay

    def fullname(self) -> str:
        return f"{self.first} {self.last}"
