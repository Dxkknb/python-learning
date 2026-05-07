"""
Python Lambdas Function
"""
from typing import Callable, List, Mapping

# TODO: First case of use

def add(x: float, y: float) -> float:
    return x + y

print(add(4, 5))

add2 = lambda x, y: x + y
print("Result:", add2(6, 7))

# TODO: Use lambda function as Higher Order Function
nums: list[int] = [3, 5, 6, 7, 8]

doubled_nums = map(lambda x: x * 2, nums)
print(list(doubled_nums))

def my_map(func: Callable[[float], float], iterable:List[float]):
    results = []

    for num in nums:
        result = func(num)
        results.append(result)

    return results

cubed = my_map(lambda x: x**3, nums)
print("Cubed:", cubed)

"""
COMMON USE CASES
"""

# TODO: Sorting with key

students : List[tuple[str, int]] = [
    ('Alice', 85),
    ('Bob', 70),
    ('Charlie', 95),
    ('Emilia', 65),
]

copy_stds = students[:]
copy_stds.sort(key=lambda student: student[1])
print("Sorted students:", copy_stds)

# TODO: Using with map()

numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print("Squared numbers:", squares)

# TODO: Using with filter()

numbers = [x * 2 for x in range(20)]
five_multiples = list(filter(lambda x: x % 5 == 0, numbers))
print("Five multiples:", five_multiples)

# TODO: Using with reduce()
from functools import reduce

numbers = [1, 2, 3, 4]
total = reduce(lambda a, b: a + b, numbers)
print("total sum:", total)

# TODO: Dictionary sorting

products = {
    "Phone": 800,
    "Laptop": 1500,
    "Tablet": 600
}
sorted_products = sorted(
    products.items(),
    key=lambda item: item[1]
)
print(sorted_products)