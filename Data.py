from Course import Course
from Department import Department
from Lecturer import Lecturer
from Student import Student

departments = {}
courses = {}
lecturers = {}
students = {}


def loadDataDpt():
    f = open('data/departments.txt', "r")
    for x in f:
        dptInfo = x.split(",")
        dptName = dptInfo[0]
        dptDomFee = dptInfo[1]
        dptIntFee = dptInfo[2]
        department = Department(dptName, float(dptDomFee), float(dptIntFee))
        departments[dptName] = department


def loadDataCrs():
    f = open('data/courses.txt', "r")
    for x in f:
        crsInfo = x.split(",")
        crsName = crsInfo[0]
        crsDptName = crsInfo[1]
        crsPoint = crsInfo[2]
        crsStudentLimit = crsInfo[3]
        course = Course(crsName,departments[crsDptName],int(crsPoint),int(crsStudentLimit))
        courses[crsName] = course


def loadDataLec():
    f = open('data/lecturers.txt', "r")
    for x in f:
        lecInfo = x.split(",")
        lecName = lecInfo[0]
        lecRate = lecInfo[1]
        lecCrsLimit = lecInfo[2]
        lecturer = Lecturer(lecName, float(lecRate), int(lecCrsLimit))
        lecturers[lecName] = lecturer


def loadDataSt():
    f = open('data/students.txt', "r")
    for x in f:
        stInfo = x.split(",")
        stName = stInfo[0]
        stBool = stInfo[1]
        stLimit = stInfo[2]

        student = Student(stName, int(stBool), int(stLimit))
        students[stName] = student


loadDataDpt()
loadDataCrs()
loadDataLec()
loadDataSt()