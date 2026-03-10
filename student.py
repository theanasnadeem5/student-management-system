students = []

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    students.append({"name": name, "roll": roll})
    print("Student added successfully")

def view_students():
    if len(students) == 0:
        print("No students found")
    else:
        for student in students:
            print(student["name"], student["roll"])

def delete_student():
    roll = input("Enter roll number to delete: ")
    for student in students:
        if student["roll"] == roll:
            students.remove(student)
            print("Student removed")

while True:

    print("\n1 Add Student")
    print("2 View Students")
    print("3 Delete Student")
    print("4 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        delete_student()

    elif choice == "4":
        break
