##def isPalindrome(x):
##    rem=0
##    a=x
##    newNumber=""
##    if(x>0):
##        while(x>0):
##            rem=x%10
##            newNumber=newNumber+str(rem)
##            x=x//10
##    else:
##        newNumber="0"
##        
##    if(newNumber==a):
##        return True
##    else:
##        return False
##    
##
##print(isPalindrome(10))
##Write a Python program to convert a given list of integers and a tuple of integers in a list of strings.
a=[1,2,3,4,5]
b=('a','b')
x=list(map(lambda c,d: str(c)+str(d), a ,b))
print(x)
##Write a Python program to create a new list taking specific elements from a tuple and
##convert a string value to integer


