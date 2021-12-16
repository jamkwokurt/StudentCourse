import sys
import mysql.connector

from Course import Course
from Department import Department
from Lecturer import Lecturer
from Student import Student

sys.stdout.write("This is a Student and Course Management System\n")


course504 = None
course502 = None
course501 = None
karsten = None
michael = None
ali = None


try:
    departmentEng = Department("engineering", 70.13, 294.90)
    course501 = Course("swen501", departmentEng, 15, 30)
    course502 = Course("swen502", departmentEng, 45, 30)
    course504 = Course("swen504", departmentEng, 60, 30)
    print(departmentEng.name + ":" + course501.name + ":" + str(course501.id) + ":" + str(course501.points))
    print(departmentEng.name + ":" + course502.name + ":" + str(course502.id) + ":" + str(course502.points))
    print(departmentEng.name + ":" + course504.name + ":" + str(course504.id) + ":" + str(course504.points))

    studentPenny = Student("Penny", True, 10)
    studentYuri = Student("Yuri", False, 10)
    studentRhea = Student("Rhea", True, 10)

    karsten = Lecturer("Karsten", 40, 4)
    michael = Lecturer("Michael", 35, 4)
    ali = Lecturer("Ali", 30, 4)

except AttributeError:
    print("Invalid attribute")


try:
    course501.enrolStudent(studentPenny)
    course502.enrolStudent(studentPenny)
    course504.enrolStudent(studentPenny)
    course501.enrolStudent(studentYuri)
    course502.enrolStudent(studentYuri)
    course504.enrolStudent(studentYuri)
    course501.enrolStudent(studentRhea)
    course502.enrolStudent(studentRhea)
    course504.enrolStudent(studentRhea)

    # print("SWEN 501 students:")
    # for student in course501.studentsEnrolled:
    #     print(student.name)
    # print("SWEN 502 students:")
    # for student in course502.studentsEnrolled:
    #     print(student.name)
    # print("SWEN 504 students:")
    # for student in course504.studentsEnrolled:
    #     print(student.name)
    michael.teachCourse(course501)
    karsten.teachCourse(course502)
    ali.teachCourse(course504)

    course501.calculateProfit()
    course502.calculateProfit()
    course504.calculateProfit()

    michael.doMarking()
    karsten.doMarking()
    ali.doMarking()

    studentYuri.getAllMarks()
    course504.getAllStudentsMarks()
    departmentEng.compareGPA()


except AttributeError:
    print("Invalid enrollment")














