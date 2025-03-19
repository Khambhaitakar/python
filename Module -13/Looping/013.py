# Write a Python program to find a specific string in the list using a simple for loop and if condition
list1 = ['apple','banana','mango']
search = 'mango'   # search Fruit

for fruit in list1:
    n= input("Enter Fruit Name: ")   #search Fruit name
    if n == search:   
        print("fruit is found on list") # condition will true then print found in list
        break    # break The loop

    else:
        print("not Found in list")  #condition is not true then print not found in list
         