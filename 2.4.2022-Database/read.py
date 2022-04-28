from databasefile import empCollection
def findGender(gender):
    data=empCollection.find({"gender":{"$eq":gender}})
    return len(list(data))
def findSalary(salary):
    data=empCollection.find({"salary":{"$gte":salary}})
    return len(list(data))

def findSort():
    data=empCollection.find().sort({"name":1})
    return list(data)

def listOfEmployee():
    data=empCollection.find()
    return list(data)
# print("No of female employee is: ",findGender("male"))
# print("No of employee above 25000",findSalary(25000))
print("sorted ",findSort())
