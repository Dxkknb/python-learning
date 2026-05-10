"""
Errors and Exceptions
"""
try:
    f = open('_corrupt_file.txt')
    if f.name == "_corrupt_file.txt":
        raise Exception("Secret file")
except FileNotFoundError as f_error:
    print(f"{f_error.filename} not found")
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print("Executing finally...")