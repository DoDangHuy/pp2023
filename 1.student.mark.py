# Student and Course class
class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob

class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.marks = {}

# Input Functions
def input_num_students():
    num_students = int(input("Enter number of students: "))
    return num_students

def input_student_info():
    id = input("Enter student id: ")
    name = input("Enter student name: ")
    dob = input("Enter student date of birth (DD/MM/YYYY): ")
    return Student(id, name, dob)

def input_num_courses():
    num_courses = int(input("Enter number of courses: "))
    return num_courses

def input_course_info():
    id = input("Enter course id: ")
    name = input("Enter course name: ")
    return Course(id, name)

def input_marks(students):
    marks = {}
    for student in students:
        mark = float(input(f"Enter mark for {student.name}: "))
        marks[student.id] = mark
    return marks

# Listing Functions
def list_courses(courses):
    print("List of courses:")
    for course in courses:
        print(f"{course.id}: {course.name}")

def list_students(students):
    print("List of students:")
    for student in students:
        print(f"{student.id}: {student.name} ({student.dob})")

def show_marks(courses, students):
    selected_course_id = input("Enter course id to show marks: ")
    selected_course = next((c for c in courses if c.id == selected_course_id), None)
    if selected_course:
        print(f"Marks for course {selected_course.name}:")
        for student_id, mark in selected_course.marks.items():
            student = next((s for s in students if s.id == student_id), None)
            if student:
                print(f"{student.name}: {mark}")
            else:
                print(f"Error: Student with id {student_id} not found.")
    else:
        print(f"Error: Course with id {selected_course_id} not found.")

# Main Program
students = []
courses = []

# Input students
num_students = input_num_students()
for i in range(num_students):
    students.append(input_student_info())

# Input courses
num_courses = input_num_courses()
for i in range(num_courses):
    courses.append(input_course_info())

# Input marks for courses
for course in courses:
    print(f"Input marks for course {course.name}:")
    marks = input_marks(students)
    course.marks = marks

# List courses and students
list_courses(courses)
list_students(students)

# Show marks for a given course
show_marks(courses, students)
