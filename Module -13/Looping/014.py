# Print this pattern using nested for loop: markdown Copy code
# *
#  **
#  ***
#  ****
#  *****
for i in range(1,6):   # row create
    for j in range(1,i+1):  # column Create
        print(" *",end="")   # star Print
    print() # for New line
    