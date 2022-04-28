
from databasefile import empCollection
from read import listOfEmployee
empCollection.update_many({"designation":"graphic designer"},{"$set":{"designation":"graphic programmer"}})
print("list of employee",listOfEmployee())
