"""
Iterators and Generators
"""

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