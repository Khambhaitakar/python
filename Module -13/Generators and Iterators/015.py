# Write a Python program that uses a custom Generator function for first 10 even numbers

def even():
    for i in range(1, 11):  # Loop from 1 to 10
        yield i * 2  # Generate even number

for num in even():   # Using the generator
    print(num)
