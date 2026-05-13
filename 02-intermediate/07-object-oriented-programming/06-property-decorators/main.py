# Entry Point

from classes import Employee

def main() -> None:

    # Create instances of class Employee
    employee_1 = Employee('John', 'Doe', 3000)
    employee_2 = Employee('Jane', 'Mike', 4500)

    employee_1.first = 'Jim'

    employee_2.fullname = 'Jane Maria Monroe'

    # Employees info
    print("--- Employees infos ---")
    print(f"Full name: {employee_1.fullname}")
    print(f"Pay: ${employee_1.pay:.2f}")
    print(f"Email: ${employee_1.email}")
    print()
    print(f"Full name: {employee_2.fullname}")
    print(f"Pay: ${employee_2.pay:.2f}")
    print(f"Email: ${employee_2.email}")

    # Delete employee 1
    del employee_1.fullname


if __name__ == "__main__":
    main()