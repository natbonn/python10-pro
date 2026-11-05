"""Add two integers."""

def main() -> None:
    """Read in two integers from user input and add them."""

    num1 = int(input("Enter first integer: "))
    num2 = int(input("Enter second integer: "))

    result = num1 + num2

    print(f"The sum of {num1} and {num2} is: {result}")


if __name__ == "__main__":
    main()