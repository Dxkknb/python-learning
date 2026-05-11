"""
Object Oriented Programming
"""

# Represent Employee

class Employee:

    num_of_employees = 0
    raise_amount = 1.04

    def __init__(self, first: str, last: str, pay: float) -> None:
        self.first = first
        self.last = last
        self.email = f"{self.first}.{last}@company.com"
        self.pay = pay

        Employee.num_of_employees += 1

    def fullname(self) -> str:
        return f"{self.first} {self.last}"

    def apply_raise_amount(self) -> None:
        self.pay = int(self.pay * self.raise_amount)