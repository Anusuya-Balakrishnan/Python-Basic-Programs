##for i in range(1,6):
##    for j in range(6,0,-1):
##        if(i>=j):
##            print("*",end=" ")
##        else:
##            print("",end=" ")
##    print()

a=0
##while(a<10):
##    print("a value",a)
##    a+=1
##    
##print(a)

a=input("Enter a number: ")
b=a.replace(',','')
print(b)
print("before type casting",type(b))
b=int(b)
print("After type casting",type(b))
