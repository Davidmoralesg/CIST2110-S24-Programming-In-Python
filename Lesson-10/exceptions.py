## Python Exceptions

# Python has a built-in error handling system called exceptions. Exceptions are
# raised when something unexpected occurs during program execution. When an
# exception is raised, the program immediately stops and the interpreter prints
# the exception message. Exceptions are useful because they tell you what went
# wrong and where it went wrong. You can use this information to fix your code
# and prevent the exception from being raised again.

# The following code raises a ZeroDivisionError exception because you cannot
# divide by zero. The interpreter prints the exception message and the program
# stops.

# print(5 / 0)  # -> uncomment this line to see the exception

# Another common exception is the FileNotFoundError exception. This exception
# is raised when a file cannot be found. The following code raises a
# FileNotFoundError exception because the file cats.txt does not exist.

# with open("cats.txt") as file_object:
#     contents = file_object.read()

# How would we handle the FileNotFoundError exception? We can use a try-except block. (This is a Try-Catch block in Java)

# Try-Except Blocks:
# The try-except block is similar to the if-else statement. The try block
# contains the code that might raise an exception. Code that depends on the
# try block executes only if the try block does not raise an exception. The
# except block tells Python what to do in case a certain exception is raised.
# The following code handles the ZeroDivisionError exception by printing a
# message instead of raising the exception.

# try is a keyword that tells Python to try to run the code in the block
try:
    print(5 / 0)
# except is a keyword that tells Python what to do if an exception is raised
except ZeroDivisionError:
    print("You cannot divide by zero!")


try:
    with open("Lesson-10/cats.txt") as file_object:
        # print("File opened successfully.")
        contents = file_object.read()
except:
    print("The file cats.txt does not exist.")

# You can also use try-except blocks to handle multiple exceptions. The
# following code handles both the FileNotFoundError and ZeroDivisionError
# exceptions.

# Note: if you use multple except blocks, the first exception that is raised will be caught by the first except block that matches the exception type

try:
    print(5 / 0)
    with open("Lesson-10/cats.txt") as file_object:
        print("File opened successfully.")
        contents = file_object.read()

except ZeroDivisionError:
    print("You cannot divide by zero!!!!!")
except FileNotFoundError:
    print("The file cats.txt does not exist.")

# the ZeroDivisionError exception is raised first, so the except ZeroDivisionError block is executed and the with open block is not executed


# try-except-else Blocks:
# You can use the else block to execute code that depends on the try block
# executing successfully. The else block executes only if the try block does
# not raise an exception. The following code uses the else block to print the
# contents of the file cats.txt if the file is opened successfully.

try:
    with open("Lesson-10/cats.txt") as file_object:
        print("File opened successfully.")
        contents = file_object.read()
except FileNotFoundError:
    print("The file cats.txt does not exist.")
else:
    print(contents)

# try-except-else-finally Blocks:
# You can use the finally block to execute code that must run regardless of
# whether an exception is raised. The finally block executes after the try
# block and any except or else blocks. The following code uses the finally
# block to print a message after the try block executes.

try:
    with open("Lesson-10/catss.txt") as file_object:
        print("File opened successfully.")
        contents = file_object.read()
except FileNotFoundError:
    print("The file cats.txt does not exist.")
else:
    print(contents)
finally:
    print("The Code for cats.txt ran")
