
def create_student(id, name, dob):
    return {'id': id, 'name': name, 'dob': dob}

def input_student_info():
    id = input("Enter student id: ")
    name = input("Enter student name: ")
    dob = input("Enter student date of birth (DD/MM/YYYY): ")
    return create_student(id, name, dob)

def list_students(students):
    print("List of students:")
    for student in students:
        print(f"{student['id']}: {student['name']} ({student['dob']})")


def create_course(id, name):
    return {'id': id, 'name': name, 'marks': {}}

def input_course_info():
    id = input("Enter course id: ")
    name = input("Enter course name: ")
    return create_course(id, name)

def list_courses(courses):
    print("List of courses:")
    for course in courses:
        print(f"{course['id']}: {course['name']}")

def input_marks(students):
    marks = {}
    for student in students:
        mark = float(input(f"Enter mark for {student['name']}: "))
        marks[student['id']] = mark
    return marks


def show_marks(courses, students):
    selected_course_id = input("Enter course id to show marks: ")
    selected_course = next((c for c in courses if c['id'] == selected_course_id), None)
    if selected_course:
        print(f"Marks for course {selected_course['name']}:")
        for student_id, mark in selected_course['marks'].items():
            student = next((s for s in students if s['id'] == student_id), None)
            if student:
                print(f"{student['name']}: {mark}")
            else:
                print(f"Error: Student with id {student_id} not found.")
    else:
        print(f"Error: Course with id {selected_course_id} not found.")

#main
students = []
courses = []

num_students = int(input("Enter number of students: "))
for i in range(num_students):
    students.append(input_student_info())

num_courses = int(input("Enter number of courses: "))
for i in range(num_courses):
    courses.append(input_course_info())

for course in courses:
    print(f"Input marks for course {course['name']}:")
    marks = input_marks(students)
    course['marks'] = marks

list_courses(courses)
list_students(students)

show_marks(courses, students)
