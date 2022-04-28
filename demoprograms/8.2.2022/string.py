a=input("enter a number: ")
b=a.replace(",","")
c=int(b)
print(c)

print(type(c))
print(c)
d=f"{c:,d}"

#print({:,}.format(c))

print(d,"its type is",type(d))
