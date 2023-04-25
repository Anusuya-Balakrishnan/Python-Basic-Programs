class Dog:
    name="Browny"
    age=3
    breed="indian"
    color="black"
    def sleep(s):
        print("dog is sleeping")
        print(s.name)
    def eat(self):
        print("dog is eating")


d1=Dog()
print(d1.name)
print(d1.age)
print(d1.breed)
d1.name="jacky"
print(d1.name)
print(d1.color)
d1.sleep()
d1.eat()

d2=Dog()
print("D2 object ",d2.name)
print(d2.age)
print(d2.breed)
print(d2.color)
