def addModify(func):
    def wrapper(*a,**b):
        print("before add function")
        print(func(*a,**b))
        print("after add function")
    return wrapper
def addModification(func):
    def wrapper(*a,**b):
        print("*"*10)
        print(func(*a,**b))
        print("*"*10)
    return wrapper

@addModification
@addModify
def add():
    return "hello how are you?"


##result=addModification(addModify(add))
add()
