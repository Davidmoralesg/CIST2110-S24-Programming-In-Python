import sys

# Simple Bank Account Management System

# Create a bank account program that will authenticate a user and allow them to deposit, check balance, and withdraw money from their account.
# Also create a Main Menu that will look like the following:
# 1. Check Balance
# 2. Deposit
# 3. Withdraw
# 4. Exit

# Functions:
# User Authentication() -> Boolean (True or False) - Return True if username and pin are correct, otherwise return False
# Main Menu - Return the user's choice (int)
# Menu Logic - attempt to call the appropriate function based on the user's choice
# Check Balance(balance) -> Float - Return the user's balance
# print Balance(balance) -> None - Print the user's balance
# Deposit(amount) -> Float - Return the user's balance after depositing the amount
# Withdraw(amount) -> Float - Return the user's balance after withdrawing the amount

# Some things to consider:
# Error Handling
# Proper Comments and Documentation
# Include main statement


# Global Variables
# Global Variables - Variables that are accessible to all functions
# In this program we will have 3 global variables
# 1. username
# 2. pin
# 3. balance
# Note: Typically Global Variables are defined with ALL CAPS

USERNAME = "JDOE52"  # Random Username
PIN = "1234"  # Random PIN
BALANCE = 1000.00  # Random Starting Balance


# Functions


# check_balance() - Function to check the user's balance
# Parameters: None
# Return Value: Float - The user's balance
def check_balance() -> float:
    """This function will return the user's balance

    Args:
        None

    Returns:
        Float: The user's balance
    """
    return BALANCE


# print_balance() - Function to print the user's balance
def print_balance() -> None:
    """
    This function will print the user's balance

    Args:
        None

    Returns:
        None
    """
    print("Your balance is: $" + str(check_balance()))


# deposit(amount) - Function to deposit money into the user's account
def deposit(amount: float = None) -> float:
    """
    This function will deposit money into the user's account

    Args:
        amount (float, optional): The amount to deposit

    Returns:
        Float: The user's balance after depositing the amount
    """
    global BALANCE  # global keyword allows us to access the global variable BALANCE (on line 35)
    if amount is None:
        amount = float(input("How much would you like to deposit? $"))
    BALANCE += amount  # Add the amount to the user's balance
    print("You have deposited $" + str(amount))
    return BALANCE


# withdraw(amount) - Function to withdraw money from the user's account
def withdraw(amount: float = None) -> float:
    """
    This function will withdraw money from the user's account

    Args:
        amount (float, optional): The amount to withdraw from the users balance.
        Defaults to None and will prompt the user to input the amount to withdraw.

    Returns:
        float: The user's balance after withdrawing the amount
    """
    global BALANCE  # global keyword allows us to access the global variable BALANCE (on line 35)
    if amount is None:
        print_balance()
        amount = input(
            "How much would you like to withdraw? $"
        )  # input is always a string
        while amount == "":
            print("You cannot withdraw $0 or a negative amount. Please try again.")
            amount = input("How much would you like to withdraw? $")
    # Edge Cases (Error Handling)
    # What if the user enters 0 or a negative number?
    # What if the user enters '' (Enter) -> This required some refactoring of the code
    while float(amount) <= 0:
        print("You cannot withdraw $0 or a negative amount. Please try again.")
        amount = float(input("How much would you like to withdraw? $"))

    # What if the user enters a number greater than their balance?
    while float(amount) > BALANCE:
        print("You cannot withdraw more than your balance. Please try again.")
        amount = float(input("How much would you like to withdraw? $"))

    BALANCE -= float(amount)  # Subtract the amount from the user's balance
    print("You have withdrawn $" + str(amount))
    return BALANCE


# main_menu() - Function to display the main menu and return the user's choice
def main_menu() -> int:
    """
    This function will display the main menu and return the user's choice

    Returns:
        int: The user's choice
    """
    print("Main Menu")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))
    # Edge Cases (Error Handling)
    # What if the user enters a number less than1 or greater than 4?
    # Use a while loop to ask the user to enter a number between 1 and 4
    while choice < 1 or choice > 4:
        print("Invalid choice. Please try again.")
        choice = int(input("Enter your choice: "))
    return choice


# Now that we have the users choice we need to design a function that will call the appropriate function based on the user's choice
# menu_logic(choice) - Function to call the appropriate function based on the user's choice
def menu_logic(choice: int) -> None:
    """
    this function calls the appropriate function based on the user's choice
    Should only be called in conjunction with the main_menu function

    Args:
        choice (int): The user's choice from the main_menu function (1-4) - this is checked in the main_menu function
    """
    if choice == 1:
        print_balance()
    elif choice == 2:
        deposit()
    elif choice == 3:
        withdraw()
    elif choice == 4:
        print("Goodbye!")
        sys.exit()


def main():
    """
    Main function to run the program
    Whatever code is in this function will run when the program is executed
    """
    print("Welcome to the Bank Account Management System")
    # print_balance()
    # deposit(500)
    # print_balance()
    # deposit()
    # print_balance()
    # withdraw()
    # print_balance()
    choice = main_menu()
    menu_logic(choice)


if __name__ == "__main__":
    main()
