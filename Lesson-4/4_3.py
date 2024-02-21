# Import Statements
# Import statements allow you to use code from other modules in your program.
import sys

# You can import sepecific functions from a module using the from keyword.
from random import randint


# Main Function
def main():
    print("Hello World")
    test_me()
    print("Python version: ", sys.version)
    sys.exit(1)


def test_me():
    print("This is a test")
    random_number = randint(1, 100)
    print(random_number)


# Create Main section of code

# Note: __name__ is a special variable that is set when the program is run.
if __name__ == "__main__":
    print("Welcome to my program!")
    main()
