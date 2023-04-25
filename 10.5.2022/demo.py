dictValue={'v':[1,2,3,4,5,6,8,10],'V1':[3,4],'V2':[1,3,7,5]}
for i in dictValue:
    a=dictValue[i]
    listValue=0
##    for j in a:
##        if(j%2==0):
    listValue=[j for j in a if(j%2==0)]
    dictValue[i]=listValue
print(dictValue)

##dictionary={1:'red',2:'green',3:'black',4:'white'}
##listValue=dictionary.items()
##listModified=[]
##for i in listValue:
##    a=list(i)
##    listModified.append(a)
##print(listModified)
