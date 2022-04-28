class Vehicle:
    def __init__(s,name,size):
        s.name=name;
        s.size=size;
        s.currentVelocity=0
        s.rrecntDirection=0
    def steer(s,direction):
        s.currentDirection=s.currentDirection+direction
        print("steer method() of vehicle class is called &\n"
              "current direction is: ",s.currentDirection)
    def move(s, velocity,direction):
        s.currentVelocity=velocity
        s.currentDirection=direction
    def getName(self):
        return self.name
    def getSize(self):
        return self.size
    def getcurrentVelocity(self):
        return self.currentVelocity
    def getcurrecntDirection(self):
        return self.currentDirection


class Car(Vehicle):
    wheels=0
    doors=0
    gear=0
    isManual=False
    currentGear=0
    def __init__(s,name,size,wheels,doors,gears,isManual):
        Vehicle.__init__(name,size)
        s.wheels=wheels
        s.doors=doors
        s.gear=gear
        s.isManual=isManual
        s.currentGear=1
    def changeGear(s,currentGear):
        print("changeGear is called")
        s.currentGear=currentGear
    def changeVelocity(s,speed,direction):
        print("changeVelocity is called")
        Vehicle.move(speed,direction)



class Outlander(Car):
    roadServiceMonths=0
    def __init__(s,roadServiceMonths):
        s.roadServiceMonths=roadServiceMonths
    def accelerate(s,rate):
        s.newVelocity=Vehicle.gecurrentVelocity(self)+s.rate
        if(s.newVelocity==0):
            Vehicle.stop()
            Car.changeGear(1)
        elif(s.newVelocity> 0 and s.newVelocity<=10):
            Car.changeGear(1)
        elif(s.newVelocity> 10 and s.newVelocity<=20):
            Car.changeGear(2)
        elif(s.newVelocity> 20 and s.newVelocity<=30):
            Car.changeGear(3)
        else:
            Car.changeGear(4)
            
        if(s.newVelocity>0):
            Car.changeVelocity(s.newVelocity,Vehicle.getCurrentDirection(self))

        
out=Outlander(36)
out.steer(45)
out.accelerate(30)
out.accelerate(20)
out.accelerate(-40)
    


