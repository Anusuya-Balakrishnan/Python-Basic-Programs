class Car(class Vehicle):
    wheels
    doors
    gear
    isManual
    currentGear
    def __init__(s,name,size,wheels,doors,gears,isManual):
        super(name,size)
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
        move(speed,direction)

class Outlander(Car):
    roadServiceMonths
    def __init__(s,roadServiceMonths):
        s.roadServiceMonths=roadServiceMonths
    def accelerate(s,rate):
        s.newVelocity=gecurrentVelocity()+s.rate
        if(s.newVelocity==0):
            s.stop()
            s.changeGear(1)
        elif(s.newVelocity> 0 and s.newVelocity<=10):
            s.changeGear(1)
        elif(s.newVelocity> 10 and s.newVelocity<=20):
            s.changeGear(2)
        elif(s.newVelocity> 20 and s.newVelocity<=30):
            s.changeGear(3)
        else:
            s.changeGear(4)
            
        if(s.newVelocity>0):
            changeVelocity(newVelocity,getCurrentDirection())
        
out=Outlander(36)
out.steer(45)
out.accelerate(30)
out.accelerate(20)
out.accelerate(-40)
    
