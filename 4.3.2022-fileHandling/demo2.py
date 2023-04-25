##f=open("data.txt","at")
##f.write("Hello world")
##f.close()

f=open("data.txt","r")
for i in f:
    print(i)
f.close()
