# initialization dictionary
student_grades = {}

# adding the student

def add_student(name, grade):

    student_grades[name] = grade

    print(f"Student name {name} added with grade {grade}")

# update student grade
def update_student(name ,grade):

    if name in student_grades:
        student_grades[name]= grade
        print(f"student name {name} updated with grade {grade}")
    else:
        print(f"student name {name} not found.")

#delete the student

def delete_student(name):

    if name in student_grades:
        del student_grades[name]
        print (f"student name {name} has been deleted successfully.")
    else:
        print("data is not found.")

#display all students

def display_students():
    if student_grades:
        print("Student Grades:")
        for name, grade in student_grades.items():
            print(f"Name: {name}, Grade: {grade}")
    else:
        print("No student data available.")

def main():
    while True:
        print("\n Student Grade Management System")

        print("1. add student")
        print("2. update student")
        print("3. delete student")
        print("4. display students")
        print("5. exit")

        choice = int(input("Enter your choice : "))

        if choice == 1:
            name = input("Enter student name: ")
            grade = input("Enter student grade: ")
            add_student(name, grade)
        elif choice == 2:
            name = input("Enter student name: ")
            grade = input("Enter new student grade: ")
            update_student(name, grade)
        elif choice == 3:
            name = input("Enter student name: ")
            delete_student(name)
        elif choice == 4:
            display_students()
        elif choice == 5:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
