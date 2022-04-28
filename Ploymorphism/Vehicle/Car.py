class Car:
    def __init__(self,cylinder,name):
        self.__cylinder=cylinder
        self.__name=name
        self.__engine=True
        self.__wheels=4

    def getCylinder(self):
        return self.__cylinder
    def getName(self):
        return self.__name
    
    def startEngine(self):
        print(self.getName(),"engine is starting")
    def accelerate(self):
        print(self.getName(), "is Accelerating")
    def brake(self):
        print(self.getName(),"is Braking")
