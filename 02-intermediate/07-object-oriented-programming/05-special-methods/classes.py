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

    def __str__(self) -> str:
        return f"{self.fullname()} - {self.pay}"

    def __repr__(self) -> str:
        return f"Employee(first={self.first}, last={self.last}, pay={self.pay})"

    def __add__(self, other: "Employee") -> float:
        return self.pay + other.pay

    def __len__(self) -> int:
        return len(self.fullname())

    def __eq__(self, other) -> bool:
        if isinstance(other, Employee):
            return self.fullname().lower() == other.fullname().lower() and self.pay == other.pay

        return NotImplemented
