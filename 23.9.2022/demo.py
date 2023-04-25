class Calc:
    def __init__(self,a,b,name):
        self.a=a
        self.b=b
        self.name=name
    def value(self,a,b):
        self.a=a
        self.b=b
    def add(s):
        print(s.a+s.b)

c=Calc(100,200,"hello")
##c.value(90,100)
c.add()

c2=Calc(49,30,"hello world")
c2.add()
