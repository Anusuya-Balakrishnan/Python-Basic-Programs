a={1:2,3:4,4:3,2:1,0:0}
li=[]
b={}
keyvalue=list(a.keys())
val=list(a.values())
for i in a.values():
    li.append(i)
for i in range(len(li)):
    for j in range(len(li)-1):
        if(li[j]>li[j+1]):
            li[j],li[j+1]=li[j+1],li[j]

for i in range(len(li)):
    b(keyvalue(val.index(i)))=i
    
print(b)
