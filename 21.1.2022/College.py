from Student import *
class College(Student):
    def __init__(self,studentName,studentid,stAge,collegeName):
        Student. __init__ (self,studentName,studentid,stAge)
        self._collegeName=collegeName
    def _displayCollegeDetails(self):
        Student._displayStudentDetails(self)
        print("College Name of the student",self._collegeName)
            
college=College("AAAA",1212,20,"BBBB")
college._displayCollegeDetails()
college=College("ABCC",1213,20,"BBBB")
college._displayCollegeDetails()
