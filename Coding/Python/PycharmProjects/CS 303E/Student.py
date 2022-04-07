# File: Student.py
# Student: Cesar Gabriel Ayala-Mendoza
# UT EID: cga773
# Course Name: CS303E
#
# Date: 3/22/22
# Description of Program: This program uses classes and objects to set and get exam grades, name of the student, and an
# average of the exams, it can print a string that shows all of the information stored from the student.


class Student:
    def __init__(self, name="None", exam1Grade="None", exam2Grade="None"):  # sets initials values for  the name, exam1,
        self.name = name                                                    # and exam2, also serves to change their
        self.exam1Grade = exam1Grade                                        # values
        self.exam2Grade = exam2Grade

    def setExam1Grade(self, exam1Grade):    # setter for the exam1 grade
        self.exam1Grade = exam1Grade

    def getExam1Grade(self):                # getter for exam1 grade, if there is no grade it returns nothing if there
        if self.exam1Grade == "None":       # is a grade it returns the grade
            return
        else:
            return print(self.exam1Grade)

    def getExam2Grade(self):                # getter for exam1 grade, if there is no grade it returns nothing if there
        if self.exam2Grade == "None":       # is a grade it returns the grade
            return
        else:
            return print(self.exam2Grade)

    def getName(self):                      # getter for the students name, it returns the student name
        return self.name

    def setExam2Grade(self, exam2Grade):    # setter for exam2 grade
        self.exam2Grade = exam2Grade

    def getAverage(self):                                               # getter for the average of the 2 tests if one
        if self.exam1Grade == "None" or self.exam2Grade == "None":      # of the tests doesn't have a value it returns
            return print("Some exam grades are not available.")         # a message saying grades are not available
        else:                                                           # if both values exist it returns the avg for
            avg = (self.exam1Grade + self.exam2Grade) / 2               # the two tests
            return print(avg)

    def __str__(self):  # String that returns all the information from the student
        return "Student: " + self.name + "\n  Exam1: " + str(self.exam1Grade) + "\n  Exam2: " + \
               str(self.exam2Grade)
