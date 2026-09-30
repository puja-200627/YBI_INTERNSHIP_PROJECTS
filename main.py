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

def view_students():
    if len(students) == 0:
        print("No students found in the list.")
        return

    for student in students:
        print("\nName:", student["name"])
        print("Roll No:", student["roll"])
        print("Branch:", student["branch"])
        
def mark_attendance():
    roll = input("Enter roll number: ")

    for student in students:
        if student["roll"] == roll:
            status = input("Enter P for Present or A for Absent: ")

            student["total_days"] += 1

            if status.upper() == "P":
                student["present"] += 1
                print("Attendance marked Present.")
            else:
                print("Attendance marked Absent.")

