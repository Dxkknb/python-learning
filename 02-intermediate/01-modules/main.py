import fibo

def main() -> None:
    # Using functions in a module
    fibo.fib(1000)

    result = fibo.fib2(100)
    print(result)

if __name__ == "__main__":
    main()