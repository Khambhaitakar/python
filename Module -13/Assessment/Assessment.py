# Create a mini-project where students combine conditional statements, loops, and functions
# to create a basic Python application, such as a simple calculator or a grade management 
# system.


students = {}  # Dictionary to store student names and their grades

def a():
    """Function to add a new student and their grades"""
    name = input("Enter student's name: ")
    grades = input("Enter student grades : ").split()
    
    # Convert grades to integers
    grades = [int(grade) for grade in grades]
    
    # Store in dictionary
    students[name] = grades
    print("Student added successfully!\n")

def c(grades):
    """Function to calculate the average grade"""
    if len(grades) == 0:
        return 0
    return sum(grades) / len(grades)

def g(average):
    """Function to determine grade category"""
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

def d():
    """Function to display all students and their details"""
    if not students:
        print("No student records found.\n")
        return
    
    print("Student Records:\n")
    for name, grades in students.items():
        average = c(grades)
        category = g(average)
        
        print("Name:", name)
        print("Grades:", grades)
        print("Average:", average)
        print("Grade Category:", category)
        print("-" * 30)

def main():
    """Main function to run the Grade Management System"""
    while True:
       menu = """
        press 1 for Add Student
        press 2 for display student
        press 3 for exit
     """
       print(menu)
        
       choice = input("Enter your choice: ")
        
       if choice == "1":
            a()
       elif choice == "2":
            d()
       elif choice == "3":
            print("Exiting the system. Goodbye!")
            break
       else:
            print("Invalid choice! Please enter a valid option.")
            break

# Run the program
main()
