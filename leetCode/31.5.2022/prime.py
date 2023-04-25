primeList=[]
def countPrimes(n):
    prime=0
    if(n>2):
        for i in range(2,n):
            count=0
            end=i//2+1
            for j in range(2,end):
                if(i%j==0):
                    count+=1
                    break
            if(count==0):
                prime+=1
                primeList.append(i)
        return prime, primeList
    else:
        return 0

print(countPrimes(499979))

