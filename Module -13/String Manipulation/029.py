# Write a Python program that manipulates and prints strings using various string methods.

# Define a string
text = "  hello Python programming  "

# Using various string methods
print(text.upper())        # Converts all characters to uppercase
print(text.lower())        # Converts all characters to lowercase
print(text.strip())        # Removes leading and trailing whitespaces
print(text.replace("Python", "Java"))  # Replaces 'Python' with 'Java'
print(text.split())        # Splits the string into a list of words
print(text.capitalize())   # Capitalizes the first letter
print(text.title())        # Capitalizes the first letter of each word
print(len(text))           # Finds the length of the string (including spaces)
print(text.startswith("  hello"))  # Checks if the string starts with "  hello"
print(text.endswith("ing  "))  # Checks if the string ends with "ing  "
