##class Landline:
##    def __init__(self,name,brand,price,access):
##        self.name=name
##        self.brand=brand
##        self.price=price
##        self.access=access
##    def call(self):
##        print("In ",self.name,"phone ,we can make a call")
##
##class Phone:
##    def __init__(self,name,brand,price,access,battery,memory):
##        self.name=name
##        self.brand=brand
##        self.price=price
##        self.access=access
##        self.battery=battery
##        self.memory=memory
##    def call(self):
##        print("In",self.name,"phone ,we can make a call")
##    def calc(self):
##        print("In ",self.name," we perform basic calculation")
##    def Fm(self):
##        print("In ",self.name," we can hear songs using Fm")

##l=Landline("n19","Nokia",2000,"fixed")
##l.call()


class Landline:
    def __init__(self,name,brand,price,access):
        self.name=name
        self.brand=brand
        self.price=price
        self.access=access
    def call(self):
        print("In ",self.name,"phone ,we can make a call")

class Phone(Landline):
    def __init__(self,name,brand,price,access,battery,memory):
        super().__init__(name,brand,price,access)
        self.battery=battery
        self.memory=memory
    def calc(self):
        print("In ",self.name," we perform basic calculation")
    def Fm(self):
        print("In ",self.name," we can hear songs using Fm")    

p=Phone("n10","Nokia",5000,"remote",4000,2)
print(p.name,p.brand)
p.call()
p.calc()
p.Fm()
