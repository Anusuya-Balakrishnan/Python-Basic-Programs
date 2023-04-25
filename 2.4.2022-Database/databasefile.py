import pymongo
client=pymongo.MongoClient('mongodb://localhost:27017')
##db=client["TataCorporation"]
##empCollection=db["Employee"]
##data1={"name":"amala",
##       "salary":30000,
##       "gender":"female",
##       "designatioin":"manager"}
##result=empCollection.insert_many([data1,data1])
##print(result.inserted_ids)


















db=client["ocean"]
Oceancollection=db["staff"]
data1={"name":"ccc","age":21, "qualification":"b.tech"}
data2={"name":"ddd","age":21, "qualification":"b.tech"}
data=[data1,data2]
oceanDoc=Oceancollection.insert_many(data)
print("database created",len(oceanDoc.inserted_ids))

