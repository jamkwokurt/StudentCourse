import itertools

counterLecturerId = itertools.count()


class Lecturer(object):
    def __init__(self, name, hourlyRate, courseLimit):
        self.name = name
        self.id = next(counterLecturerId)
        self.hourlyRate = hourlyRate
        self.courseTeaching = []
        self.courseLimit = courseLimit

    def __str__(self):
        return self.name

    def teachCourse(self, course):
        if len(self.courseTeaching) < self.courseLimit:
            self.courseTeaching.append(course)
            course.lecturers.append(self)
        else:
            print("Failed to teach course " + self.name + ". " + "Number reached limit!")

    def doMarking(self):
        if not (len(self.courseTeaching) == 0):
            print("You're marking as " + self.name + " and course you teach listed below: ")
            for i in range(len(self.courseTeaching)):
                print(str(i + 1) + ". " + self.courseTeaching[i].name)

                selection = int(input("Please select a course to mark: "))
                if 0 < selection < len(self.courseTeaching) + 1:
                    course = self.courseTeaching[selection - 1]
                    if not course.isMarked:
                        for student in course.studentsEnrolled:
                            print("Student name: " + student.name + " id: " + str(student.id))
                            mark = float(input("Please input mark:"))
                            student.allMarks[course.name] = mark
                            print("Student name: " + student.name + " id: " + str(student.id) + " marked: " + str(mark))

                        course.isMarked = True
                    else:
                        print("Course already marked")
                else:
                    print("Invalid course selection")

        else:
            print("No course on record")