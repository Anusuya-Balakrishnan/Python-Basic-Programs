import functools
a=[3,45,6,7,8,2,43]
##def maxValue(a,b):
##    if(a>b):
##        return a
##    else:
##        return b
##
##x=functools.reduce(maxValue,a)
##print(x)

a=[2,3,4,5,6]
##def even(a):
##    if(a%2==0):
##        return True
##c=lambda x: x%2==0
x=list(filter(lambda x: x%2!=0,a))
print(x)

