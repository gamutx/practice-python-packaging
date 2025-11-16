"""Main entry point for the application."""

from my_package import hello_world, add_numbers


if __name__ == "__main__":
    hello_world("Developer")
    result = add_numbers(5, 3)
    print(f"5 + 3 = {result}")