##a=[1,2,3,4,5,6,7,8,9,10]
##def even(s):
##    return s%2==0
##def odd(s):
##    return s%3==0
##
##
##b=list(filter(lambda x:x%3==0,a))
##print(b)
##
##b=list(filter(odd,a))
##print(b)

##a=["Apple", "Banana", "Pear", "Apricot", "Orange"]
##def stringwitha(s):
##    return (s[0]=="a" or s[0]=="A")
##
##print(list(filter(stringwitha,a)))
##print(list(filter(lambda x:(x[0]=="a" or x[0]=="A"),a)))
##
##a=[1,2,3,4,5,6,7,8,9,10]
##def numbers(n):
##    return n*4
##
##print(list(map(numbers,a)))
##b=list(map(lambda x:x*4,a))
##print(b)

##from functools import *
##
##a=[1,2,3,4,5,6,7,8,9,10]
##b=reduce(lambda a,b:a+b,a)
##print(b)
from functools import reduce
employee=[{"name":"abi","salary":20000,"yearsOfService":2},{"name":"siva","salary":30000,"yearsOfService":5},
          {"name":"sathya","salary":40000,"yearsOfService":6},{"name":"anusuya","salary":10000,"yearsOfService":6}]
salary=[]
for i in employee:
    print(i)

for i in employee:
    salary.append(i["salary"])
    
salaryupdated=list(map(lambda x:x*2,salary))

for i in range(len(employee)):
    employee[i]["salary"]=salaryupdated[i]
print("Salary incremented")
for i in employee:
    print(i)
  
print("total salary details of employees of the company")
print(reduce(lambda x,y:x+y,salary ))



























