"""
Entry point
"""

from classes import Employee

def main() -> None:
    # Create instances of class Employee
    employee_1 = Employee('John', 'Doe', 3000)
    employee_2 = Employee('Jane', 'Mike', 4500)

    # Apply some raises amount
    employee_1.apply_raise_amount()
    employee_2.apply_raise_amount()

    # Print infos
    print(f"----- {Employee.num_of_employees} Employees infos -----")
    print(f"Fullname: {employee_1.fullname()}")
    print(f"Pay: ${employee_1.pay}")
    print()
    print(f"Fullname: {employee_2.fullname()}")
    print(f"Pay: ${employee_2.pay}")

if __name__ == "__main__":
    main()