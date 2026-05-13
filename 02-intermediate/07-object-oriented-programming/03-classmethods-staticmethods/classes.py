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

    def display_employee(self) -> None:
        for prop, value in self.__dict__.items():
            print(f"{prop}: {value}")

    @classmethod
    def set_raise_amount(cls, amount: float) -> None:
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str: str, separator="-") -> "Employee":
        first, last, pay = emp_str.split(separator)
        return cls(first, last, float(pay))

    @staticmethod
    def is_work_day(day: int) -> bool:
        return not (day == 5 or day == 6)
