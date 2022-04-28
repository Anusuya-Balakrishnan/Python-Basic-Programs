class Student:
    def __init__(self,name,idNum,age):
        self.__name=name
        self.__idNum=idNum
        self.__age=age
    def _setName(self,name):
        self.name=name
    def _setidNum(self,idNum):
        self.idNum=idNum
    def _setAge(self,age):
        self.age=age
    def _displayStudentDetails(self):
        print("Name of the student: ",self.__name)
        print("ID Number of the student: ",self.__idNum)
        print("Age of the student: ",self.__age)


