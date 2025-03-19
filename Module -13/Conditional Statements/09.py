# Write a Python program to calculate grades based on percentage using if-else ladder.

n = float(input("Enetr Percentage: "))

if n>=95:
    print("Grade: A+")

elif n>=80:
    print("Grade: A")

elif n>=70:
    print("Grade: B")

elif n>=60:
    print("Grade: c")

elif n>=50:
    print("Grade: D")

elif n>=33:
    print("You Are pass")

elif n>=0:
    print("Fail")

else:
    print("in valid choice")

