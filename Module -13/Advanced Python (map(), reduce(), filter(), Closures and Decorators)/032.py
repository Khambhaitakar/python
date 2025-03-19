# Write a Python program that filters out even numbers using the filter() function.
# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using filter() to keep only odd numbers
odd = list(filter(lambda x: x % 2 != 0, numbers))

# Print the result
print(odd)
