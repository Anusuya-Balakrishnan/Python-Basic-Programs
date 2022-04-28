a=int(input("enter first number: "))
b=int(input("enter second number: "))
try:
    c=a/b
    if(c==0):
        raise ArithmeticError
except ArithmeticError as a:
    print(a)
else:
    print(a,"is divided by ",b,"=",c)
finally:
    print("Finally program executed")
                        
