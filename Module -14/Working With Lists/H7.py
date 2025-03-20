# Write a Python program to insert elements into an empty list using a for loop and append().
l= []  # empty list

n = int(input("Enter the number of : "))  # add The how many elements do you need

for i in range(n):
    print("Enter Number",i+1,":",end="") # entre the value 
    el = input() # el input The values
    l.append(el)  # append is update the list

print(l)  # print list


