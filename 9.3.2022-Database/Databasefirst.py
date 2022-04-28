
import pymongo
client = pymongo.MongoClient("mongodb+srv://root:root@cluster0.rhwqd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db=client["TravelAgencey"]
UserDetails=db["UserDetails"]

print("database connected")
# data={"name":"priya","age":20,"location":"chennai"}
# UserDetails.update_many({"age":20},{"$inc":{"age":2}})
data=UserDetails.find().sort({"name":1,"age":-1})
print(list(data))
