students = []


def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    branch = input("Enter branch: ")

    student = {
        "name": name,
        "roll": roll,
        "branch": branch,
        "present": 0,
        "total_days": 0,
        "marks": {}
    }

    students.append(student)
    print("Student added successfully!")


