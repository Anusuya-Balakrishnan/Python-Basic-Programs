import pymongo

client=pymongo.MongoClient("mongodb://localhost:27017")

mydb=client["StudentDatabase"]
mycol=mydb["Student Information"]

data=[{"_id":1002,"name":"AAAA","age":21,"mark":440},{"_id":1003,"name":"BBBB","age":21,"mark":440}]

##mycol.insert_many(data)
##x=mycol.find({"name":{"$gt":"X"}})
##for i in x:
##    print(i)
##oldData={"mark":440}
##newData={"$set":{"mark":445}}
##x=mycol.update_many(oldData,newData)
##print(x.modified_count,"updated")

x=mycol.find().sort("mark",-1)

for i in x:
    print(i)
