empList=[{'empname':'ccc','empid':5,'empsalary':30000,'designation':'leader'},
         {'empname':'aaa','empid':2,'empsalary':25000,'designation':'Manager'},
         {'empname':'bbb','empid':8,'empsalary':28000,'designation':'Director'}]
salary=[]
empName=[]
empId=[]
for i in empList:
    salary.append(i['empsalary'])
    empName.append(i['empname'])
    empId.append(i['empid'])
salary.sort()
empId.sort()
maxSalary=salary[len(salary)-1]
minSalary=salary[0]

##Maximum and Minimum salary of employee

print("Maximum and Minimum salary of employee:\nmaximum salary is",maxSalary)
print("minimum salary is",minSalary)


##Search employee name in a list

findName=input("enter name of employee to search")
for i in range(len(empName)):
    if(findName ==empName[i]):
        print("Employee name:",empList[i]['empname'],'\nEmployee id:',empList[i]['empid'],
              '\nEmployee Salary:',empList[i]['empsalary'],'\nEmployee Designation:',empList[i]['designation'])
    elif(i==(len(empName))):
        print("invalid input")
    
##Sorting
SortedEmpList=[]
for i in range(len(empId)):
    for j in range(len(empList)):
        if(empId[i]==empList[j]['empid']):
            SortedEmpList.append(empList[j])

print(SortedEmpList)
    
