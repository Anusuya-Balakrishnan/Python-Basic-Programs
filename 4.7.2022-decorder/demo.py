def outer(func):
    def inner(a,b):
        if(b!=0):
            return func(a,b)
        else:
            return 0
    return inner



@outer
def div(a,b):
    print("hello")
    return a/b

print(div(2,0))


