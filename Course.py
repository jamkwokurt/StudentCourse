import itertools

from Student import Student

counterCourseId = itertools.count()


class Course(object):
    def __init__(self, name, department, points, studentLimit):
        self.name = name
        self.department = department
        department.courses.append(self)
        self.id = next(counterCourseId)
        self.studentLimit = studentLimit
        self.isMarked = False
        validPoints = [15, 20, 30, 40, 45, 60]

        if points not in validPoints:
            raise AttributeError("Invalid points input")
        else:
            self.points = points
        self.studentsEnrolled = []
        self.lecturers = []
        self.allStudentsMarks = {}

        self.roomCostPerPoint = 500;
        self.profit = 0;


    def __str__(self):
        return self.name + ": id: " + self.id

    def enrolStudent(self, student):
        if not isinstance(student, Student):
            raise AttributeError("Invalid enrollment")
        else:
            if len(self.studentsEnrolled) < self.studentLimit:
                self.studentsEnrolled.append(student)
                student.addCourse(self)
            else:
                print("Failed to enrol student " + student.name + ". " + "Number reached limit!")

    def getAllStudentsMarks(self):
        for student in self.studentsEnrolled:
            self.allStudentsMarks[student.name] = student.allMarks[self.name]

        marks = self.allStudentsMarks
        for e in range(len(marks)):
            print(([marks for marks in marks.keys()][e], [marks for marks in marks.values()][e]))

    def calculateProfit(self):
        roomCostTotal = self.roomCostPerPoint * self.points
        lecturerCostTotal = 0
        for lecturer in self.lecturers:
            lecturerCostTotal = lecturer.hourlyRate * self.points * 10 + lecturerCostTotal;
        self.profit = self.profit - roomCostTotal - lecturerCostTotal

        print(self.name + " course profit " + " = " + str(self.profit))