# Write a Python program to count how many times each character appears in a string. 

t = "python programming"
d ={}

for d in t:
    d[chr]=d(chr,0)+1

print(d)