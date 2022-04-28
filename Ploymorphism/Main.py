from Vehicle.Car import *

class Mitsubishi(Car):
    """def __init__(self,cylinder,name):
        Car.__init__(self,cylinder,name)"""
    pass
        
class Holden(Car):
    """def __init__(self,cylinder,name):
        Car.__init__(self,cylinder,name)"""
    pass    
class Ford(Car):
    """def __init__(self,cylinder,name):
        Car.__init__(self,cylinder,name)"""
    pass

car=Car(8,"Base Car")
car.startEngine()
car.accelerate()
car.brake()
print()
mitsubishi=Mitsubishi(6,"Outlander VRX 4WD")
mitsubishi.startEngine()
mitsubishi.accelerate()
mitsubishi.brake()
print()
ford=Ford(6,"Ford Falcon")
ford.startEngine()
ford.accelerate()
ford.brake()
print()
holden=Holden(6,"Holden Commodore")
holden.startEngine()
holden.accelerate()
holden.brake()

