##try:
##    f=open("text.txt",'r')
##except Exception as e:
##    print(e)
##else:
##    print(f.read())

##a=[1,2,3,4,5,6,7,8]
##number=int(input("Enter position of number: "))
##try:
##    print(a[number])
##except:
##    print("Out of range")
##finally:
##    print("Program executed successfully")
##

##try:
##    a=int(input("enter a number:"))
##    b=int(input("enter a number:"))
##except Exception as e:
##    print(e)
##    print("Accept only Integer")
##else:
##    c=a+b
##    print(a," + ",b," = ",c)
##finally:
##    print("program executed Successfully")
##
##while(True):
##    a=int(input("Enter a number"))
##    try:
##        if(a>=0 and a<=1000):
##            pass
##        else:
##            raise Exception   
##    except Exception:
##        print(a,"is out of range(0 to 1000)")
##        continue
##    else:
##        print(a)
##        break
##    finally:
##        print("program executed Successfully")


age=int(input("enter your age: "))
try:
    if(age!=int(age)):
        raise Exception
except Exception as e:
    print(age,"Not Accepted Value")
    print("Accept age value in integer only")
else:
    print("Your age is ",age)
    


try:
    a=int(input("enter a number: "))
    if(a<=-1 or a!=int(a)):
        raise Exception
except Exception:
    print("Invalid Value")
else:
    print("The Number is:",a)











