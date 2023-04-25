import re
##address="535 E Globe Ave,Cincinnati,OH 45220"
address="1711 PROSPECT AVE, Sonoma,CA 95476"
addressList=re.split("[,]",address)
addressKey=["street","city"]
addressKey_2=["state","zipCode"]
state_zip=re.split("\s",addressList[len(addressList)-1])
addressMap={}
for i in range(2):
    addressMap[addressKey[i]]=addressList[i]
for i in range(len(state_zip)):
    addressMap[addressKey_2[i]]=state_zip[i]
print(addressMap)

 
import usaddress
value=usaddress.parse("1711 PROSPECT AVE, Sonoma,CA 95476")
##print(value)
street=""
for tupleValue in value:
    if(tupleValue[1]=="PlaceName"):
        placeNameIndex=value.index(tupleValue)
        break
    else:
        if(street==""):
            street=tupleValue[0]
        else:
            street+=" "+tupleValue[0]

addressKey=["city","state","zipcode"]
address={}
address["street"]=street
index=0
for i in range(placeNameIndex,len(value)):
    address[addressKey[index]]=value[i][0]
    index+=1
print(address)



    
