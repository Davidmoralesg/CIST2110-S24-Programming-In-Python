# In python we have the ability to work with dates and times using the datetime module.
# How do we work with dates and times in Python?
# Importing the datetime module
# import datetime

import datetime as dt  # -> popular alias for the datetime module

# We can get the current date and time using the now() method
now = dt.datetime.now()
print(now)

# notice how the date and time is formatted
# we can format the date and time using the strftime() method
# strftime() takes in an argument called a format code

# In the examples below i will be interracting with the now variable with is a datetime object

# Example 1
# format the date and time

print(now.strftime("%Y-%m-%d %H:%M:%S"))  # Output: 2021-10-06 14:45:00

# Just print date, hour, and minute
print(now.strftime("%Y-%m-%d %H:%M"))  # Output: 2021-10-06 14:45

# Make the date look like were used to seeing it
print(now.strftime("%m/%d/%Y"))  # Output: 03/28/2024

# Make the time in 12hr format
print(now.strftime("%I:%M %p"))  # Output: 02:45:00 PM


# Example 2
# Where datetime starts to get really useful is when we need to compare dates and times

date_1 = dt.datetime(2021, 10, 6)  # -> October 6, 2021

# Compare to the current date
print(date_1 < now)  # -> True
print(date_1 > now)  # -> False

# How many days until October 6, 2021?
print((date_1 - now).days)  # This will be negative because date_1 is in the past

date_2 = dt.datetime(2024, 10, 6)  # -> October 6, 2024

# how many days until October 6, 2024?
print((date_2 - now).days)  # This will be positive because date_2 is in the future


# Example 3
# We can create functions that return days until a certain date
# for example lets try how many days until end of the year


def days_until_end_of_year():
    # Get the current date
    now = dt.datetime.now()
    # Create a variable to hold the end of the year date
    end_of_year = dt.datetime(now.year, 12, 31)
    # Return the difference in days
    return (end_of_year - now).days


print(days_until_end_of_year())
