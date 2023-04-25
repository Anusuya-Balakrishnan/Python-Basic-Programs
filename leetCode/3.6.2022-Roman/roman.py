def romanToInt(s):
    roman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    sub={"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
    result=0
    temp=""
    for i in range(len(s)):
        if(s[i:i+2] in sub):
            result+=int(sub[s[i:i+2]])
            temp=s[i+1]
        else:
            if(temp==s[i]):
                temp=""
            else:
                result+=int(roman[s[i]])
    return result

inputValue=input("enter roman value")
print("the result",romanToInt(inputValue))

##def intToRoman(x):
##    roman={1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M"}  
##    sub={4:"IV",9:"IX",40:"XL",90:"XC",400:"CD",900:"CM"}
##    stringX=str(x)
##    result=""
##    for i in range(len(stringX)):
##        temp=int(stringX[i])*(10**(len(stringX)-(i+1)))
##        if(temp in roman):
##            result+=roman[temp]
##        elif(temp in sub):
##            result+=sub[temp]
##        else:
##            romanKey=list(roman.keys())
##            print("i loop")
##            for j in range(len(romanKey)):
##                r=0
##                q=0
##                if(temp<romanKey[j]):
##                    print("j loop")
##                    q=temp//romanKey[j-1]
##                    print("q",q)
##                    r=temp%romanKey[j-1]
##                    print("r",r)
##                    if(r in romanKey):
##                        result+=(q*roman[romanKey[j-1]])+(roman[r])
##                        break
##                    elif(r>romanKey[j-2]):
##                        result+=(q*roman[romanKey[j-1]])+((r//romanKey[j-2])*roman[romanKey[j-2]])
##                        break
##                    else:
##                        result+=(q*roman[romanKey[j-1]])+((r)*roman[romanKey[j-2]])
##                    break   
##    return result
####print(intToRoman(3))
####print(intToRoman(58))
######print(intToRoman(126))
##print(intToRoman(2000))
