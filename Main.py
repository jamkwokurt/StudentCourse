import sys
import Data
from Student import Student

sys.stdout.write("This is a Student and Course Management System\n")

departmentEng = None
swen504 = None
swen502 = None
swen501 = None
michael = None
karsten = None
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
        if not len(department.courses) == 0:
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
            print("There is no course under this department yet.")
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
    print("Please select course to print marking:")
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
    print("Please select student to print marking:")
    for i in range(len(students)):
        print(str(i + 1) + ". " + students[i].name)
    selectionSt = int(input())
    indexSt = selectionSt - 1
    if 0 <= indexSt < len(students):
        students[indexSt].getAllMarks()
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
        if not len(department.courses) == 0:
            department.compareGPA()
        else:
            print("There is no course under this department yet.")
    else:
        print("Invalid department input")


def calculateProfit():
    print("Please select course to print marking")
    for i in range(len(courses)):
        print(str(i + 1) + ". " + courses[i].name)
    selectionCrs = int(input())
    indexCrs = selectionCrs - 1
    if 0 <= indexCrs < len(courses):
        course = courses[indexCrs]
        course.calculateProfit()
    else:
        print("Invalid selection")


# def createStudent():
#     print("Please input student name, student type (0 for international and 1 for domestic) "
#           "and course limit seperated by space")
#     studentAttributes = input().split(" ")
#     name = studentAttributes[0]
#     isDomestic = studentAttributes[1]
#     courseLimit = studentAttributes[2]
#     newStudent = Student(name, isDomestic, courseLimit)
#     f = open("data/students.txt", "a")
#     f.write("\n" + name + "," + isDomestic + "," + courseLimit)
#     f.close()


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
        # elif selection == "9":
        #     createStudent()
        else:
            print("Invalid selection input. Please start over")
            showMenu()


showMenu()
