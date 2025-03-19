# Write a Python program that uses a custom iterator to iterate over a list of integers.
numbers = [10, 20, 30, 40, 50]  # List of integers

# Getting an iterator from the list
iterator = iter(numbers)

# Iterating manually without exception handling
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
