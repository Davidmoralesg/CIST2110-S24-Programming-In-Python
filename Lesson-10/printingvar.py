# In python there are multiple ways to print variables.

# 1. You can use the print() function to print variables directly.
# 2. You can use the f-string method to print variables.
# 3. You can use the format() method to print variables.

# Example 1
first_name = "Greg"
last_name = "Walsh"

# Method 1
print("Method 1")
print(first_name)
print(last_name)
print(first_name, last_name)
print(first_name + " " + last_name)  # String concatenation

# Method 2 the f-string method
print("Method 2")
print(f"{first_name} {last_name}")

# Method 3 the format() method
print("Method 3")
print("hello my first name is {} and last name is {}".format(first_name, last_name))


# f-strings with loops and conditionals
# You can use f-strings with loops and conditionals to print variables in a loop

# for loop
for i in range(1, 11):
    print(
        f"Hellow world! My name is {first_name} and my last name is {last_name} and the number is {i}"
    )
