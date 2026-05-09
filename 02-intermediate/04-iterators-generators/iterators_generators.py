"""
Iterators and Generators
"""
import time

# Iterator
s = 'abc'
it = iter(s)

print(it)

print(next(it)) # a
print(next(it)) # b
print(next(it)) # c
#print(next(it)) # Raise StopIteration error

# Add iterator to a class

class Reverse:
    """Iterator fo looping over a sequence backwards"""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

rev = Reverse("Hello")

for char in rev:
    print(char)

class GenericIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.iterator)

fruits = GenericIterator(['Mango', 'Papaya'])

for fruit in fruits:
    print(fruit)

"""
Classic Iterators
"""

# List Iterator
class ListIterator:
    def __init__(self, sequence):
        self.sequence = sequence
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.sequence):
            raise StopIteration

        value = self.sequence[self.index]
        self.index += 1

        return value

numbers = [10, 20, 30]

iterator = ListIterator(numbers)

for num in iterator:
    print(num)

# Tuple Iterator

class TupleIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration

        value = self.data[self.index]
        self.index += 1

        return value

names = ('Annie', 'Julie', 'Jack', 'John')

for name in TupleIterator(names):
    print(name)

# Range Iterator

class RangeIterator:
    def __init__(self, start: int, stop: int | None = None, step: int = 1) -> None:
        if stop is None:
            start, stop = 0, start

        self.current = start
        self.stop = stop
        self.step = step

    def __iter__(self) -> "RangeIterator":
        return self

    def __next__(self):
        if self.step > 0 and self.current >= self.stop:
            raise StopIteration

        if self.step < 0 and self.current <= self.stop:
            raise StopIteration

        value = self.current
        self.current += self.step

        return value


print("Range Iterator:")
for i in RangeIterator(10):
    print(i)


# Enumerate Iterator
from typing import Iterable, Any

class EnumerateIterator:
    def __init__(self, iterable, start: int=0):
        self.iterable = iterable
        self.index = start
        self.position = 0

    def __iter__(self) -> "EnumerateIterator":
        return self

    def __next__(self):
        if self.index >= len(list(self.iterable)):
            raise StopIteration

        result = (self.index, self.iterable[self.position])

        self.index += 1
        self.position += 1

        return result


for i, value in EnumerateIterator(['a', 'b', 'c'], start=1):
    print(f"{i} => {value}")

# Generators

def get_items(items: dict):
    for _key, _value in items.items():
        yield _key, _value

items_gen = get_items({'Bob': 25, 'John': 30, 'Doe': 40, 'Julie': 17})
items = []

while True:
    try:
        items.append(next(items_gen))
        print(items)
    except StopIteration:
        print("End of data fetching...")
        break
    time.sleep(2)