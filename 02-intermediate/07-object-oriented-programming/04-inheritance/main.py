"""
Entry point
"""

from classes import Developer, Manager


def main() -> None:
    # Create instances of class Developer
    dev_1 = Developer('Konan', 'Bernard', 90_000, 'Python')
    dev_2 = Developer('Maria', 'Kane', 80_000, 'Java')
    dev_3 = Developer('Antoine', 'Jonathan', 110_000, 'C#')

    # Apply raise amount
    print(f"Dev 1 pay before applying raise amount: ${dev_1.pay}")
    dev_1.apply_raise_amount()
    print(f"Dev 1 pay after applying raise amount: ${dev_1.pay}")

    # Create a manager
    manager_1 = Manager('Sue', 'Smith', 120_000, [dev_1])
    manager_1.add_employee(dev_2)
    manager_1.print_employees()

if __name__ == "__main__":
    main()
