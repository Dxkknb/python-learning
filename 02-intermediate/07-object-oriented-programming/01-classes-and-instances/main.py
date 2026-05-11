# Entry Point

from classes import Employee

def main() -> None:

    # Create instances of class Employee
    employee_1 = Employee('John', 'Doe', 3000)
    employee_2 = Employee('Jane', 'Mike', 4500)

    # Employee objects
    print(employee_1)
    print(employee_2)

    # Employees info
    print("--- Employees infos ---")
    print(f"Full name: {employee_1.fullname()}")
    print(f"Pay: ${employee_1.pay:.2f}")
    print()
    print(f"Full name: {employee_2.fullname()}")
    print(f"Pay: ${employee_2.pay:.2f}")

if __name__ == "__main__":
    main()