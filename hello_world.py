"""_summary_
Python program to print "Hello World" and test the environment.
"""

# Import statements go here
import sys

# Module constants go here
# Name of the program
__program_name__ = "Hello World"
# Version of the program
__version__ = "0.1"
# Author of the program
__author__ = "Greg Walsh"


# Function definitions go here
def main():
    """_summary_
    Main function for the program.
    """
    print("Hello World")  # Print "Hello World"
    print("Python version: ", sys.version)  # Print the Python version


# Main section of code goes here
# If this is the main program being run, call the main() function
if __name__ == "__main__":
    main()


# This code can be ran from the command line by typing:
# python hello_world.py
# This will print:
# Hello World
# Python version:  3.11.4 (main, Jul 25 2023, 17:36:13) [Clang 14.0.3 (clang-1403.0.22.14.1)]


# This code can be ran from VSCode by clicking the green play button in the top right corner of the editor.
# It will launch a terminal and run the code.

# This is a test commit
