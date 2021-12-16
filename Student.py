import itertools

counterStudentId = itertools.count()


class Student(object):
    def __init__(self, name, isDomesticStudent, courseLimit):
        self.name = name
        self.id = next(counterStudentId)
        self.isDomesticStudent = isDomesticStudent
        self.courseEnrolled = []
        self.courseLimit = courseLimit
        self.allMarks = {}

    def __str__(self):
        return self.name + ": id: " + self.id

    def addCourse(self, course):
        self.payForCourse(course)
        if len(self.courseEnrolled) < self.courseLimit:
            self.courseEnrolled.append(course)
        else:
            print("Failed to add course " + course.name + ". " + "Number reached limit!")

    def payForCourse(self, course):
        feePerPoint = 0;
        if self.isDomesticStudent:
            feePerPoint = course.department.feePerpointDom
        else:
            feePerPoint = course.department.feePerpointInt

        feeTotal = course.points * feePerPoint
        course.profit = course.profit + feeTotal

    def getAllMarks(self):
        print("All marks for student name: " + self.name + " id: " + str(self.id) + ":")
        if not len(self.allMarks.values()) == 0:
            marks = self.allMarks
            for e in range(len(marks)):
                print(([marks for marks in marks.keys()][e], [marks for marks in marks.values()][e]))
        else:
            print("No marks on record")
