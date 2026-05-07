import fibo
from utils import get_name, greeting as greet

def main() -> None:
    # Using functions in a module
    fibo.fib(1000)

    result = fibo.fib2(100)
    print(result)

    # More on Modules
    firstname = input("Your firstname: ")
    lastname = input("Your lastname: ")

    if firstname or lastname:
        fullname = get_name(firstname, lastname)
        print(greet(fullname))

if __name__ == "__main__":
    main()