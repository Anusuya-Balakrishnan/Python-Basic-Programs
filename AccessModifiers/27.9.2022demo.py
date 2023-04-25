##class Triangle:
##    def __init__(self):
##        self.side1=3
##        self.side2=4
##        self.side3=5
##    
##    def area(self):
##        return self.side1*self.side2*self.side3
##    def perimeter(self):
##        return self.side1+self.side2+self.side3
##
##
##t=Triangle()
##print(t.area())
##print(t.perimeter())
class Parent:
    def __init__(self,parentName):
        self.parentName=parentName

class Child(Parent):
    def __init__(self,parentName,childName):
##        Parent.__init__(self,parentName)
        super().__init__(parentName)
        self.childName=childName
class GrandChild(Child):
    def __init__(self,parentName,childName,grandChildName):
        super().__init__(parentName,childName)
        self.grandChildName=grandChildName
         
p=Parent("Ram")
print(p.parentName)
c=Child("Ram","Arul")
print(c.parentName)
print(c.childName)

g=GrandChild("Ram","Arun","Arjun")
print(g.parentName)
print(g.childName)
print(g.grandChildName)
