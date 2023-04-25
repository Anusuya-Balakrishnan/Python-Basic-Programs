def myString(name):
   count=0
   for i in name:
      count+=1
   print(count)
myString("Hiocean")


##a=[]
##n=int(input("enter the range of list"))
##for i in range(0,n):
##   b=int(input("enter the value"))
##   a.append(b)
##print(a)
##a.reverse()
##print(a)

##rows = 6
##for num in range(1,rows):
##    for i in range(1,num+1):
##        print(num, end=" ")
##    print(" ")


##for i in range(1,5):
##    for j in range(1,i+1):
##        print("* ",end="")
##    print()



##str = "OCEAN"
##i = 0
##while(i<len(str)):
##   print(str[i])
##   i+=1

##n=int(input("Enter the range"))
##i=1
##while i<=n:
##      print("number=",i,"square=",i*i)
##      i+=1


##n=int(input("Enter the range"))
##i=1
##while i<=2*n:
##    if i%2==0:
##        print(i)
##    i+=1


##
##n=int(input("Enter the range"))
##i=1
##while i<=n:
##    print(i)
##    i+=1


##age=int(input("Enter your age"))
##if age >=60:
##    print("Senior Citizen")
##else:
##    print("Not a Senior Citizen")


##for i in range(1,4):
##    for j in range (1,4):
##        print("* ",end="")
##    print()
##


##num=int(input("enter the number"))
##result=0
##temp=num
##while num>0:
##    rem=num%10
##    result= result*10+rem
##    num=num//10
##if (temp==result):
##    print("given number is palindrome")
##else:
##    print("given number is not palindrome")



##string=input("enter the string:")
##newString=''
##length=len(string)-1
##for i in range(length,-1,-1):
##    newString+=string[i]
##if(newString==string):
##    print("palindrome")
##else:
##    print("not palindrome")

##sum=0
##i=1
##while i<=10:
##    sum=sum+i
##    i+=1
##print("Sum =",sum)



##a=-1
##b=1
##n=int(input("Enter the number"))
##for i in range(1,n+1):
##    c=a+b
##    a=b
##    b=c
##    print(c)
##

##num1 = int(input("Enter first number"))
##if num1 > 0 :
##    print("Number is positive")
##elif num1<0:
##    print("Number is negative")
##else:
##    print("Number is Zero")
##x = input('Enter value of x: ')
##y = input('Enter value of y: ')
##temp = x
##x = y
##y = temp
##print('The value of x after swapping:',x)
##print('The value of y after swapping:',y)


##import random
##print("random number generate from 0 to 9:",random.randint(0,9))


##import random
##print("random number generate from 0 to 9:",random.randint(0,9))
##

##length=int(input("enter the value of length:"))
##breadth=int(input("enter the value of breadth:"))
##area=length*breadth
##print("Area of rectangle",area)

##num=int(input("enter the number:"))
##cube_root=num**(1/3)
##print("cube root of",num,"is",cube_root)


##yr=int(input("Enter the year"))
##if yr%100==0:
##    if yr%400==0:
##          print("Entered year is leap year")
##    else:
##          print("Entered year is not a leap year")
##else:
##    if yr%4==0:
##         print("Entered year is leap year")  
##    else:
##        print("Entered year is not a leap year")

##principle=int(input("enter the principle amount:"))
##number_Of_Years=int(input("enter the number of years:"))
##rate_Of_Interest=int(input("enter the rate of interest:"))
##simple_Interest=principle*number_Of_Years*rate_Of_Interest/100
##print("Simple Interest =",simple_Interest)


##n=int(input("enter the range"))
##n1=int(input("enter the number"))
##i=1
##while i<=n:
##    print(i,"x",n1,"=",i*n1)
##    i+=1
##
##
##

##base=int(input("enter the base value:"))
##height=int(input("enter the height value:"))
##area=(base*height)/2
##print("Area of triangle",area)




##num = float(input('Enter a number: '))
##num_sqrt = num ** 0.5
##print('The square root of %{num} is %0.3f'%(num_sqrt))



##num = int(input("Enter a number: "))
##factorial = 1
##if num < 0:
##   print("Sorry, factorial does not exist for negative numbers")
##elif num == 0:
##   print("The factorial of 0 is 1")
##else:
##   for i in range(1,num + 1):
##       factorial = factorial*i
##   print("The factorial of",num,"is",factorial)
##




##a=int(input("enter the value of a"))
##b=int(input("enter the value of b"))
##c=int(input("enter the value of c"))
##if a>=b and a>=c:          
##    print("A is greater than B and C")
##elif b>=a and b>=c:
##    print("B is greater than A and C")
##else:
##    print("C is greater than A and B")



##num=int(input("Enter the number"))
##if num%2==0:
##   print("Number is Even")
##else:
##   print("Number is Odd")



##num1=int(input("enter the value of number1:"))
##num2=int(input("enter the value of number2:"))
##addition=num1+num2
##print("Addition:",addition)
