"""
With the while loop we can execute a set of statements as long as a condition is true
"""

# The while loop

i = 1
while i < 6:
    print(i)
    i += 1

# The break statement

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# The continue statement

i = 1
while i < 6:
    i += 1
    if i % 2 == 0:
        continue
    print(i)

# The else Statement
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")