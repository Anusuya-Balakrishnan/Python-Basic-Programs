from databasefile import empCollection
data1={"name":"amala",
       "salary":30000,
       "gender":"female",
       "designatioin":"manager"}
data2={"name":"raju",
       "salary":20000,
       "gender":"male",
       "designatioin":"graphic designer"}
data3={"name":"uma",
       "salary":30000,
       "gender":"female",
       "designatioin":"supervisor"}
data4={"name":"divya",
       "salary":20000,
       "gender":"female",
       "designatioin":"graphic designer"}
data5={"name":"vidya",
       "salary":20000,
       "gender":"female",
       "designatioin":"supervisor"}
data6={"name":"bala",
       "salary":30000,
       "gender":"male",
       "designatioin":"marketing manager"}
data7={"name":"ravi",
       "salary":50000,
       "gender":"male",
       "designatioin":"marketing head"}
empCollection.insert_many([data1,data2,data3,data4,data5,data6,data7])
