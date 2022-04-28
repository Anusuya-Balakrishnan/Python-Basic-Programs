import os
f=open("test.txt",'wt')
f.write("\n Hello World")
f.write("\n Happy Morning")
f.write("\n Text Message")
f.write("\n End......")
f=open("test.txt",'r')
print(f.read())
f=open("test.txt",'wt')
f.write("Good Morning")
f.write("\n End......")
f=open("test.txt",'r')
print(f.read())

f=open("test.txt",'rb')
_text_="test.txt"
print(f.read())
print("file name: ",os.path.basename(_text_))
print("diectory name: ",os.path.dirname(test.txt))

