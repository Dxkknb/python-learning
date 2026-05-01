"""
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.
"""

# Create a lambda function

multiply = lambda a, b: a * b
print(multiply(10, 12))

# Usecase

def multiply_by(num: int) -> int:
    return lambda a: a * num

double = multiply_by(2)
print(double(11))

# Lambda with Built-in Functions

numbers: list[int] = [1, 2, 3, 4, 5]

doubled: list[int] = list(map(lambda num: num * 2, numbers))
print(numbers, " => ", doubled)

even_numbers: list[int] = list(filter(lambda num: num % 2 == 0, numbers))
print("Initial list:",numbers, "=>", "Filtered list:", even_numbers)

students = [
    ("Alice", 20, [15, 18, 12, 14, 16]),
    ("Brian", 23, [10, 9, 13, 11, 12]),
    ("Catherine", 21, [17, 19, 18, 16, 20]),
    ("Daniel", 24, [8, 14, 10, 12, 9]),
    ("Sophia", 22, [13, 15, 14, 16, 17])
]

sort_by_age = sorted(students, key=lambda student: student[1])
print("Sort by age:", sort_by_age)

sort_by_name = sorted(students, key=lambda student: student[0])
print("Sort by name:", sort_by_name)

sort_by_name_length = sorted(students, key=lambda student: len(student[0]))
print("Sort by student name length:", sort_by_name_length)

# Sort by mean
def mean(notes: list[int]) -> float:
    try:
        return round(sum(notes)/len(notes), 2)
    except ZeroDivisionError:
        print("Notes list must contain a value!")
    return 0

sort_by_mean = sorted(students, key=lambda student: mean(student[2]))

for student in sort_by_mean:
    print(f"{student[0]} -> {mean(student[2])}")