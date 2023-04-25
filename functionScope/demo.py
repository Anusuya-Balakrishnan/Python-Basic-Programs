##a=120
##def add():
##    global a
##    a=80
##    print("local variable",a)
##
##add()
##print("global variable",a)
##x="global"
##def outer():
##    x = "local"
##    def inner():
##        nonlocal x
##        x="hello"
##        print("inner:", x)
##
##    inner()
##    print("outer:", x)
##
##
##outer()
##print(x)
import functools

list1=[10,20,30,40,50]

def addList(a,b):
    return a+b

result=functools.reduce(addList,list1)
print(result)
