# Write a Python program to convert two lists into one dictionary using a for loop.

l = [1,2,3] # list1 for keys 
l1 = ["Harsh","Darshan","Shlok"] # list2 for values
d={} # empty Dictionary

for i in range(len(l)):  # condition 
    d[l[i]] = l1[i] 

print(d) # print Dictionaries