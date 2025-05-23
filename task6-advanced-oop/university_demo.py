from person import Person
from student import Student
from course import Course
from instructor import Instructor
from enrollment import Enrollment
from random import randint
students = []
courses = []
instructors = []
enrollments = []
genders = ["M", "F"]

cor = ["English601", "Bio001", "CS16602", "PHY202", "EEE22"]
for i in range(1, 11):  # Create 10 students
    s = Student(student_id=i, student_name=f"Student{i}", student_age=18+i, student_sex="M" if i % 2 == 0 else "F")
    students.append(s)
for i in range(1, 11):  # Create 10 random instructors
    s = Instructor(i, f"instructor{i}", i+25, genders[(randint(0,1))], cor[randint(0,3)])
    instructors.append(s)
for i in range(1, 11):  # Create 10 random courses
    s = Course(i, randint(0, 4))
    courses.append(s)

#Printing all objects in our university
print("Students")
for student in students:
    print(student)
    
print("instructors")
for instructor in instructors:
    print(instructor)

print("Courses")
for course in courses:
    print(course)
    
print("enrollments")

for student in students:
    course = courses[randint(0, len(courses)-1)]
    course_name = course.course_name
    course_id = course.course_id
    enrollments.append(Enrollment(student.id, student.name, student.age,student.sex, course_id, course_name, "2025-01-01"))

for enrollment in enrollments:
    print(enrollment)
    
    