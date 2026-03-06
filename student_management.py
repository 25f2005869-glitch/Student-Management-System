# Load students from file
try:
    with open("students.txt", "r") as file:
        students = file.read().splitlines()
except FileNotFoundError:
    students = []

def show_menu():
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    # Add student
    if choice == "1":
        name = input("Enter student name: ")
        students.append(name)

        with open("students.txt", "a") as file:
            file.write(name + "\n")

        print("Student added successfully!")

    # View students
    elif choice == "2":
        if students:
            print("\nStudent List:")
            for s in students:
                print("-", s)
        else:
            print("No students found.")

    # Search student
    elif choice == "3":
        search = input("Enter student name to search: ")
        if search in students:
            print("Student found!")
        else:
            print("Student not found.")

    # Delete student
    elif choice == "4":
        delete_student = input("Enter student name to delete: ")
        if delete_student in students:
            students.remove(delete_student)

            with open("students.txt", "w") as file:
                for s in students:
                    file.write(s + "\n")

            print("Student deleted successfully!")
        else:
            print("Student not found.")

    # Exit
    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")
