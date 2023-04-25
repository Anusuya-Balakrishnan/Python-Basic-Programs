##def outer(func):
##    print("outer function is running")
##    def inner():
##        print("inner function is running")
##        func()
##        print("inner function is completed")
##    return inner
##@outer
##def hello():
##    print("hello world")
##
####ref=outer(hello)
####ref()
##
####hello()
def outerDecorator(func):
    def innerDecorator(a,b):
        print("*"*10)
        func(a,b)
        print("*"*10)
    return innerDecorator


def outer(func):
    def inner():
        a=int(input("enter a value"))
        b=int(input("enter b value"))
        if(a>0 and b>0):
            func(a,b)
        else:
            print("not able to add two numbers")
    return inner

@outer
def add(a,b):
    print("sum of two number ",a+b)

add()
