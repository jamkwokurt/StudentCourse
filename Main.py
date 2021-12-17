import sys

import Data
from Course import Course
from Department import Department
from Lecturer import Lecturer
from Student import Student

sys.stdout.write("This is a Student and Course Management System\n")

departmentEng = None
swen504 = None
swen502 = None
swen501 = None
karsten = None
michael = None
ali = None
studentPenny = None
studentYuri = None
studentRhea = None




try:
    departments = list(Data.departments.values())
    lecturers = Data.lecturers
    courses = list(Data.courses.values())
    students = list(Data.students.values())
    studentIDMap = {}
    for student in students:
        studentIDMap[str(student.id)] = student

    # departmentEng = Department("Engineering", 70.13, 294.90)
    # departments.append(departmentEng)

    # michael = Lecturer("Michael", 35, 4)
    # karsten = Lecturer("Karsten", 40, 4)
    # ali = Lecturer("Ali", 30, 4)
    #
    # lecturers["Michael"] = michael
    # lecturers["Karsten"] = karsten
    # lecturers["Ali"] = ali
    #
    # swen501 = Course("SWEN501", departmentEng, 15, 30)
    # swen502 = Course("SWEN502", departmentEng, 45, 30)
    # swen504 = Course("SWEN504", departmentEng, 60, 30)
    # courses.append(swen501)
    # courses.append(swen502)
    # courses.append(swen504)
    # print(departmentEng.name + ":" + swen501.name + ":" + str(swen501.id) + ":" + str(swen501.points))
    # print(departmentEng.name + ":" + swen502.name + ":" + str(swen502.id) + ":" + str(swen502.points))
    # print(departmentEng.name + ":" + swen504.name + ":" + str(swen504.id) + ":" + str(swen504.points))
    #
    # studentPenny = Student("Penny", 1, 10)
    # studentYuri = Student("Yuri", 0, 10)
    # studentRhea = Student("Rhea", 1, 10)
    # students.append(studentPenny)
    # students.append(studentYuri)
    # students.append(studentRhea)
    # studentIDMap[str(studentPenny.id)] = studentPenny
    # studentIDMap[str(studentYuri.id)] = studentYuri
    # studentIDMap[str(studentRhea.id)] = studentRhea


except AttributeError:
    print("Invalid attribute")


# try:
# except AttributeError:
#     print("Invalid input")

def assignLecturer():
    for lecturer in lecturers.values():
        print("Please select course to assign to " + lecturer.name + " (separate by space for multiple course)")
        for i in range(len(courses)):
            print(str(i + 1) + ". " + courses[i].name)
        selections = input().split(" ")
        for selection in selections:
            index = int(selection)
            if 0 < index < len(courses) + 1:
                lecturer.teachCourse(courses[index - 1])
            else:
                print("Invalid selection")


def enrolStudent():
    # list departments and ask user to select
    for i in range(len(departments)):
        print(str(i + 1) + ". " + departments[i].name)
    print("Please select department to start:")
    selectionDpt = int(input())
    indexDpt = selectionDpt - 1
    if 0 <= indexDpt < len(departments):
        department = departments[indexDpt]
        print(department.name + " selected")
        # list courses offered by selected department and ask user to choose
        for i in range(len(department.courses)):
            print(str(i + 1) + ". " + department.courses[i].name)
        print("Please select course to continue:")
        selectionCrs = int(input())
        indexCrs = selectionCrs - 1
        if 0 <= indexCrs < len(department.courses):
            course = courses[indexCrs]
            print(course.name + " selected")
            # list all students with id and ask for user input to enrol
            for student in students:
                print(str(student.id) + ". " + student.name)
            print("Please input student ids separated by space:")
            ids = input().split(" ")
            if not len(ids) == 0:
                for id in ids:
                    student = studentIDMap[id]
                    course.enrolStudent(student)
            else:
                print("Invalid ID input")
        else:
            print("Invalid course input")
    else:
        print("Invalid department input")


def recordGrade():
    print("Please enter lecturer name and id seperated by space to start marking: ")
    lecturerStr = input().split(" ")
    print(lecturerStr[0])
    if lecturers.keys().__contains__(lecturerStr[0]):
        lecturerName = lecturerStr[0]
        lecturers[lecturerName].doMarking()
    else:
        print("Lecturer information not found")


def printCourseGrades():
    print("Please select course to print marking")
    for i in range(len(courses)):
        print(str(i + 1) + ". " + courses[i].name)
    selectionCrs = int(input())
    indexCrs = selectionCrs - 1
    if 0 <= indexCrs < len(courses):
        course = courses[indexCrs]
        course.getAllStudentsMarks()
    else:
        print("Invalid selection")


def printStudentsGrades():
    print("Please select student to print marking")
    for i in range(len(students)):
        print(str(i + 1) + ". " + students[i].name)
    selectionSt = int(input())
    indexSt = selectionSt - 1
    if 0 <= indexSt < len(students):
        student = students[indexSt]
        student.getAllMarks()
    else:
        print("Invalid selection")


def compareGPA():
    for i in range(len(departments)):
        print(str(i + 1) + ". " + departments[i].name)
    print("Please select department to start:")
    selectionDpt = int(input())
    indexDpt = selectionDpt - 1
    if 0 <= indexDpt < len(departments):
        department = departments[indexDpt]
        print(department.name + " selected")
        department.compareGPA()


def calculateProfit():
    print("Please select course to print marking")
    for i in range(len(courses)):
        print(str(i + 1) + ". " + courses[i].name)
    selectionCrs = int(input())
    indexCrs = selectionCrs - 1
    if 0 <= indexCrs < len(courses):
        course = courses[indexCrs]
        course.calculateProfit()


def showMenu():
    while True:
        print("=========== Menu ==========")
        print("1. Assign Lecturer")
        print("2. Enrol Student")
        print("3. Record Grades")
        print("4. Print Course Grades")
        print("5. Print Student Grades")
        print("6. Compare GPA")
        print("7. Calculate Profit")
        print("8. Go Back to Menu")
        print("Please select from menu: ")
        selection = input()
        if selection == "1":
            assignLecturer()
        elif selection == "2":
            enrolStudent()
        elif selection == "3":
            recordGrade()
        elif selection == "4":
            printCourseGrades()
        elif selection == "5":
            printStudentsGrades()
        elif selection == "6":
            compareGPA()
        elif selection == "7":
            calculateProfit()
        elif selection == "8":
            showMenu()
        else:
            print("Invalid selection input. Please stat over")
            showMenu()


showMenu()


















