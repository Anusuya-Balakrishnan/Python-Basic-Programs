"""Write a statement in Python to declare a dictionary
whose keys are 1, 2, 3 and values are Jan, Feb and Mar respectively."""
a=int(input("enter no of items in dictionary: "))
dict1={}
for i in range(a):
    b=input("enter value for key")
    dict1[i]=b

print(dict1)
