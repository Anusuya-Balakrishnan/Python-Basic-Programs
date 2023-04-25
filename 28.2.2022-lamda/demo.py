##def add(a,b):
##    return a+b
##
##print(add(5,6))
##


##
##
##x=lambda a,b,c,d: a+b+c+d
##print(x(2,6,2,3))
##print(x(2,30,4,5))
##
##mydoubler=lambda a: a*2
##print(mydoubler(5))

a=("apple","banana","cherry")
##length=[]
##for i in a:
##    length.append(len(i))
##print(length)

def myFunc(n):
    return len(n)

mylist=map(myFunc,a)
print(list(mylist))

number=[12,23,34,12,34,67]
def myFunc(n):
    return n+2

x=list(map(myFunc,number))
print(number)
print(x)
