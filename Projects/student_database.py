student_data = [
    {"name": "Alice", "age": 20, "grades": [85, 90, 78], "attendance_percentage": 80.0},
    {"name": "Bob", "age": 22, "grades": [70, 65, 68], "attendance_percentage": 60.5},
    {"name": "Charlie", "age": 21, "grades": [92, 88, 91], "attendance_percentage": 95.0}
]

def add_student():
    name = input("What is the name of the student?: ")
    age = input("What is the age of the " + str(name) + " ?: ")
    grade = []
    for subject in ["math", "english", "dutch"]:
        grade.append(input("What is " + str(name) + " his/her grade for " + str(subject) + "?: "))
    attendance_percentage = input("What is " + str(name) + " attendance percentage?: ")
    student_data.append(dict({"name": name, "age": age, "grades": grade, "attendance_percentage": attendance_percentage}))
    show_students()

def remove_students():
    student_to_search = input("What is the name of the student you would like to remove?: ")
    i = 0
    index_to_remove = -1
    while i < len(student_data):
        if student_to_search == student_data[i].get("name"):
            index_to_remove = i
            break
        else:
            i = i + 1
    if index_to_remove != -1:
        student_data.pop(index_to_remove)
        show_students()
    else:
        print("Student not found")

def show_students():
    print("\nThis is a list of the students we have in the current database: ")
    for students in student_data:
        print(str(students.get("name") + " (" +  str(students.get("age")) + ")"))
    print("\n")

#This is the main executable. Above are the helper functions
while True:
    prompt = input("What would you like to do?:\n \
A. Add a student to the database\n \
B. Remove a student from the database\n \
C. Show the students\n ")
    if prompt == "A":
        add_student()
    elif prompt == "B":
        remove_students()
    elif prompt == "C":
        show_students()
