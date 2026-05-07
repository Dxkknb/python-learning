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