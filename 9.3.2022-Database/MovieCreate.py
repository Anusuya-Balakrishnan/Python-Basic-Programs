from pymongo import MongoClient

client=MongoClient("mongodb+srv://root:root@cluster0.rhwqd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db=client["TicketBooking"]
Movie=db["MovieCollection"]
# Movie.insert_one({"name":"Beast","lang":"Tamil","duration":"3.00hrs","rating":3 })
Movie.replace_one({"duration":"3.00hrs"},{"duration":"3.15hrs"})
print("movie replaced")