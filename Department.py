class Department(object):
    def __init__(self, name, feePerpointDom, feePerpointInt):
        self.name = name
        self.feePerpointDom = feePerpointDom
        self.feePerpointInt = feePerpointInt
        self.courses = []
        self.result = {}

    def __str__(self):
        return self.name

    def addCourse(self, course):
        self.courses.append(course)
        course.department = self

    def compareGPA(self):
        gpaMap = {}

        for course in self.courses:
            courseMarkSum = 0
            for student in course.studentsEnrolled:
                courseMarkSum = courseMarkSum + student.allMarks[course]
            courseGPA = courseMarkSum / len(course.studentsEnrolled)
            gpaMap[course.name] = courseGPA

        gpaSum = 0
        for gpa in gpaMap.values():
            gpaSum = gpaSum + gpa
        gpaAve = gpaSum / len(self.courses)
        higher = []
        equal = []
        lower = []
        self.result["higher"] = higher
        self.result["equal"] = equal
        self.result["lower"] = lower
        for nameCourse, gpaCourse in gpaMap.items():
            if gpaCourse > gpaAve:
                self.result["higher"].append(nameCourse)
            elif gpaCourse == gpaAve:
                self.result["equal"].append(nameCourse)
            else:
                self.result["lower"].append(nameCourse)

        print("Courses that have GPAs higher than the department average:")
        for course in self.result["higher"]:
            print(course)
        print("Courses that have GPAs equal to the department average:")
        for course in self.result["equal"]:
            print(course)
        print("Courses that have GPAs lower than the department average:")
        for course in self.result["lower"]:
            print(course)