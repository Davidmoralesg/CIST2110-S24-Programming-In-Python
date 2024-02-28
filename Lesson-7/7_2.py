import pytest


# Imagine we have a add function that adds 2 numbers and returns the result

# 1. Write a basic test that ensures the function returns the correct result

# first example of pytest (notice assert statement)


def test_add():
    assert add(2, 3) == 5


# run this code in your terminal with the following command:
# pytest 7_2.py
# This is a red test, meaning it fails. We need to write the add function to make it pass.

# 2.  Write the add function so that the test passes
# This is the green phase


def add(a, b):
    return a + b


# 3. Write a test that ensures the function raises a TypeError if the arguments are not numbers


def test_add_type_error():
    with pytest.raises(TypeError):
        add("two", 3)


# Imagine we have a function that multiples 2 numbers and returns the result.


# Red phase
def test_multiply():
    assert multiply(2, 3) == 6


# Green phase
def multiply(a, b):
    return a * b


# Refactor Phase / Edge Cases


# Imagine we have a function that subtracts 2 numbers and returns the result.
# Red phase
def test_subtract():
    assert subtract(5, 3) == 2


# Green phase
def subtract(a, b):
    return a - b


# Refactor Phase / Edge Cases


# Imagine we have a function that divides 2 numbers and returns the result.
# Red phase
def test_divide():
    assert divide(6, 3) == 2


# Green phase
def divide(a, b):
    return a / b


# Refactor Phase / Edge Cases
# What if the user tries to divide by 0?


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(6, 0)


# Imagine we ahve a function that compares two numbers and returns the result as a boolean
def test_compare():
    assert compare(5, 5) == True
    assert compare(5, 6) == False


def compare(a, b):
    return a == b
