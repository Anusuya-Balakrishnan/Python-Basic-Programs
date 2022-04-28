import pymongo
client=pymongo.MongoClient('mongodb+srv://root:root@cluster0.rhwqd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db=client["TataCorporation"]
empCollection=db["Employee"]


















# db=client["ocean"]
# Oceancollection=db["staff"]
# data1={"name":"aaa","age":21, "qualification":"b.tech"}
# oceanDoc=Oceancollection.insert_one(data1)
# print("database created")

