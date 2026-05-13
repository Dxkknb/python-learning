"""
Object Oriented Programming
"""


# Represent Employee

class Employee:

    def __init__(self, first: str, last: str, pay: float) -> None:
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def fullname(self) -> str:
        return f"{self.first} {self.last}"

    @property
    def email(self):
        return f"{self.first}.{self.last}@company.com".replace(" ", "_")


    @fullname.setter
    def fullname(self, name: str) -> None:
        first, *last = name.split(' ')
        self.first = first

        if last:
            new_last = " ".join(last)
            self.last = new_last
        else:
            self.last = ''

    @fullname.deleter
    def fullname(self) -> None:
        print("Delete Name!")

        self.first = ""
        self.last = ""
