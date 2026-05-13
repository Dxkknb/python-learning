import re


def is_valid_username(name: str) -> bool:
    pattern = r'^[a-zA-Z0-9]{4,}$'
    return bool(re.fullmatch(pattern, name))


def get_username() -> str:
    while True:
        username = input("Username: ")

        if is_valid_username(username):
            return username
        else:
            print("Provide a valid username!")
