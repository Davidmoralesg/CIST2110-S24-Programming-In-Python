# In python you can split strings into lists using the split() method

# Example 1
# Splitting a string into a list
string = "Hello, World!"
print(string.split(","))  # Output: ['Hello', ' World!']

string2 = "Hello World! My name is Greg Walsh"
print(
    string2.split()
)  # Output: ['Hello', 'World!', 'My', 'name', 'is', 'Greg', 'Walsh']

list1 = string2.split()

for word in list1:
    print(word)

print(string2.split("!"))  # Output: ['Hello World', ' My name is Greg Walsh']

# notice there is a space before the word My in the output
# this is because the split method splits the string at the character specified

# you can use the strip() method to remove the whitespace

string3 = "         Hello World! My name is Greg Walsh          "
print(string3)
print(string3.strip())

print(string2.split("!"))

string_split = string2.split("!")
for word in string_split:
    print(word.strip())
