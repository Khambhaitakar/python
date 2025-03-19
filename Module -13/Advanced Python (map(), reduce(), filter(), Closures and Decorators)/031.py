# Write a Python program that uses reduce() to find the product of a list of numbers.

from functools import reduce

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Using reduce() to find the product
product = reduce(lambda x, y: x * y, numbers)

# Print the result
print(product)
