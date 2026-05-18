"""A simple application that calculates the sum of two numbers."""


def get_number(prompt):
    """Ask the user for a number and keep trying until the input is valid."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def main():
    """Run the sum calculator application."""
    print("Simple Sum Calculator")
    print("---------------------")

    first_number = get_number("Enter the first number: ")
    second_number = get_number("Enter the second number: ")
    total = first_number + second_number

    print(f"The sum of {first_number} and {second_number} is {total}.")


if __name__ == "__main__":
    main()
