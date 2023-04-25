class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        Student.college="PEC"

a=Student("abi",20)
b=Student("siva",20)
print(a.name)
print(a.college)
print(b.college)
a.college="Christ"
print()
print(a.college)
print(b.college)
Student.college="SMVC"
print()
print(a.college)
print(b.college)

print(Student.__main__)
