class Student:
    def __init__(self,name,age,mark):
        self.name=name
        self.age=age
        self.mark=mark
    def printDetails(self):
        print("Student name: ",self.name,"\nage: ",self.age,"\nmark: ",self.mark)

class School(Student):
    def __init__(self,name,age,mark,school):
        Student.__init__(self,name,age,mark)
        self.school=school
    def printDetails(self):
        Student.printDetails(self)
        print("School name: ",self.school)


school=School("aaaa",23,95,"abc school")
school.printDetails()
