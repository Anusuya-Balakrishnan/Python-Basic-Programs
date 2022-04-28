##a=input("enter a string: ")
##for i in range(len(a)):
##    if(a[i]=="."):
##        for j in range(i+1,len(a)):
##            if(a[j]==","):
##                temp=a[i]
##                temp1=a[j]
##                a[i]=temp1
##                a[j]=temp
##                break
##    elif(a[i]==","):
##        for j in range(i+1,len(a)):
##            if(a[j]=="."):
##                temp=a[i]
##                temp1=a[j]
##                a[i]=temp1
##                a[j]=temp
##                break
##    else:
##        print("not able to swap the . and ,")
