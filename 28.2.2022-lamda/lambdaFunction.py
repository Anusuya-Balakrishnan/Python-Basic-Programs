a=[1,2,3,4,5,6,7]

def functionValue():
    global a
    a=[4,5,6,6,7]

    print("inside the function",a)


functionValue()
print("outside the function",a)
