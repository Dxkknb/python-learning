"""
Entry point
"""

from classes import Employee


def main() -> None:
    # Create instance of class Employee
    employee_1 = Employee('John', 'Doe', 3000)
    employee_2 = Employee('Jane', 'Smith', 4500)

    print(repr(employee_1))
    print(str(employee_1))

    print("Total salaries:", employee_1 + employee_2)

    print("Total length name:", len(employee_1))

    if employee_1 == employee_2:
        print("Employee 1 and Employee 2 are the same object")
    else:
        print("Employee 1 and Employee 2 are different objects")


if __name__ == "__main__":
    main()
