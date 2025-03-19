# Write a Python program to skip 'banana' in a list using the continue statement. List1 = ['apple', 'banana', 'mango']

l= ['apple', 'banana', 'mango']

for i in l:
    if i == 'banana':
        continue

    print(i)