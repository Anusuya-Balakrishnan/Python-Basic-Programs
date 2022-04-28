a={1:100,2:5,3:79,4:32}
keysOfa=a.keys()
tem=0
for i in keysOfa:
    tem=a[i]
    if(a[i]>a[i]):
        a[i]=a[i+1]
        a[i+1]=tem

print(a)
