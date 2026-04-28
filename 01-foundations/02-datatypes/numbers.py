"""
There are tree numeric types in python
   - int
   - float
   - complex
"""

# Int and Float

products = "Clothes"
product_quantity = 12
product_price = 1.75 # In dollar

total_price = product_quantity * product_price

print(f"""
------------------------- INVOICE -------------------------------
    Product: {products}
    Quantity: {product_quantity}
    Product price: ${product_price}
    Total: ${total_price}
""")

# Check the type of variable
print(f"Type of {product_quantity}: {type(product_quantity)}")
print(f"Type of {product_price}: {type(product_price)}")

# Complex
x = 3 + 5j
y = 5j
z = -3j

print(f"Square module of {x}: {x.real ** 2 + x.imag ** 2}")
print(f"conjugate of {y} + {z}: {(y + z).conjugate()}")