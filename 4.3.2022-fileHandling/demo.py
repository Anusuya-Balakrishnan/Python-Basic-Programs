
##f.write("My file is started")
##f1=open("flower1.JPG",'rb')
##f2=open("picture.jpg",'wb')
##for i in f1:
##    f2.write(i)
##    
##f1.close()    
##f2.close()
##print("file created")
##f.close()
f=open("text.txt","r+")
f.write("Hello program")
print(f.read())
