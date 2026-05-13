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

    # Before changing the global raise amount
    print(f"Raise amount: {Employee.raise_amount}")
    print(f"Employee 1 raise amount: {employee_1.raise_amount}")
    print(f"Employee 2 raise amount: {employee_2.raise_amount}")

    # After changing the class raise amount
    Employee.set_raise_amount(1.07)
    print(f"Raise amount: {Employee.raise_amount}")
    print(f"Employee 1 raise amount: {employee_1.raise_amount}, Pay: {employee_1.pay}")
    print(f"Employee 2 raise amount: {employee_2.raise_amount}, Pay: {employee_2.pay}")

    # Using class method as an alternative constructor
    emp_str_1 = 'John-Jonas-9000'
    emp_str_2 = 'Steve-Smith-30000'
    emp_str_3 = 'Jane-Morris-75500'

    new_emp_1 = Employee.from_string(emp_str_1)
    new_emp_2 = Employee.from_string(emp_str_2)
    new_emp_3 = Employee.from_string(emp_str_3)

    for emp in (new_emp_1, new_emp_2, new_emp_3):
        emp.display_employee()

    # Check if it's a work day
    from datetime import datetime

    if Employee.is_work_day(int(datetime.now().weekday())):
        print("It's work day")
    else:
        print("It's week-end")


if __name__ == "__main__":
    main()