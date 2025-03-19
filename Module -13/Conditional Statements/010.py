# Write a Python program to check if a person is eligible to donate blood using a nested if.
age = int(input("Enter Age: "))
Weight = float(input("Enter Your weight: "))

if age>=18:
     if Weight>=45:
        print("Eligible for donate Blood")
     else:
        print("Not Eligible for donate Blood")

else:
    print("invalid Age!!")

