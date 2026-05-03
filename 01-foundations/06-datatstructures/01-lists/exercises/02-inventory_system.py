""" TODO: Inventory Management System"""

from typing import TypeAlias
from enum import Enum
import re

# Type
Product: TypeAlias = list[str | int]  # [name, quantity, price]

# Add / remove
def add_product(products: list[Product], handler):
    def __add_product(products: list[Product], name: str, qty: int, price: float) -> list[Product]:
        products.append([name, qty, price])
        return products
    
    name, qty, price = handler()    
    return __add_product(products, name, qty, price)

def remove_product(products: list[Product], handler) -> list[Product]:
    name: str = handler()
    products[:] = [p for p in products if p[0] != name]
    
    return products

# Out of stock
def find_out_of_stock(products: list[Product]) -> list[Product]:
    return [p for p in products if p[1] == 0]

# Total inventory value
def total_inventory_value(products: list[Product]) -> float:
    return sum(p[1]*p[2] for p in products)

# Most expensive product
def most_expensive_product(products: list[Product]) -> Product:
    return max(products, key=lambda p: p[2])

def apply_discount(products: list[Product], handler) -> list[Product]:
    name, percent = handler()

    for p in products:
        if name == "all" or p[0].lower() == name.lower():
            p[2] = round(p[2] * (1 - percent / 100))
    
    return products


def main() -> None:
    # Data
    products: list[Product] = [
        ["Laptop", 15, 750000], ["Mouse", 40, 5000], ["Keyboard", 25, 18000],
        ["Monitor", 8, 185000], ["Headphones", 30, 22000], ["Webcam", 12, 35000],
        ["USB Hub", 50, 8500], ["SSD 1TB", 20, 65000], ["RAM 16GB", 18, 42000],
        ["Mousepad", 60, 3500], ["Desk Lamp", 0, 12000], ["Printer", 5, 95000],
        ["Scanner", 0, 75000], ["Router", 14, 28000], ["Switch 8P", 9, 22000],
        ["Surge Protector", 35, 6500], ["External HDD", 22, 48000], ["Tablet", 3, 210000],
        ["Smartphone", 0, 320000], ["Smartwatch", 7, 145000],
    ]

    # Handlers
    def valid_product_name(product_name: str) -> bool:
        pattern = r"^[a-zA-Z]{3,50}(\s[a-zA-Z]{3,50})?$"
        return re.fullmatch(pattern, product_name)
    
    def product_infos() -> tuple[str | int | float]:
        while True:
            try:
                name: str = input("Product name: ")
                qty: int = int(input("Product quantity: "))
                price: float = float(input("Product price: "))
            except ValueError:
                print("Name or quantity or price are invalid.")

            if valid_product_name(name) and qty >= 0 and price > 0:
                return name, qty, price
            else:
                print("Invalid name or quantity or price")
                print("Provide valid items")
    
    def product_name():
        while True:
            try:
                name: str = input("Product name: ")
            except ValueError:
                print("Name is invalid.")

            if valid_product_name(name):
                return name
            else:
                print("Provide a valid product name")
                continue


    def discount_infos():
        name = product_name()
        while True:
            try:
                discount: float = float(input("Discount: "))

                if (0 < discount and discount >= 100):
                    print("Impossible!")
                    print("Discount must be between 0 and 100")
                else:
                    return name, discount
            except ValueError:
                print("Discount is invalid.")


    # Enum
    class Options(Enum):
        ADD_PRODUCT = 1
        REMOVE_PRODUCT = 2
        OUT_OF_STOCK = 3
        MOST_EXPENSIVE_PRODUCT = 4
        APPLY_DISCOUNT = 5
        EXIT = 6

    OPTIONS: str = """
1. Add product
2. Remove product
3. Out of stock
4. Most expensive product
5. Apply discount
6. Exit
"""

    actions = {
        Options.ADD_PRODUCT.value: lambda: add_product(products, product_infos),
        Options.REMOVE_PRODUCT.value: lambda: remove_product(products, product_name),
        Options.OUT_OF_STOCK.value: lambda: find_out_of_stock(products),
        Options.MOST_EXPENSIVE_PRODUCT.value: lambda: most_expensive_product(products),
        Options.APPLY_DISCOUNT.value: lambda: apply_discount(products, discount_infos)
    }

    print(OPTIONS)
    while True:
        try:
            choice: str = int(input("Choose an option: "))

            if Options.EXIT.value == choice:
                print("Quit inventory system")
                break
            
            action = actions.get(choice)

            if action:
                result = action()
                print(result)
        except ValueError:
            print("Type a valid option number.")


if __name__ == "__main__":
    main()