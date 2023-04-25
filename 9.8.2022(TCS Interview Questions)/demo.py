input1=input("enter a string")
couple=0
time=0
for i in range(len(input1)-1):
    pair=input1[i:i+2]
    
    if((pair=="fm" or pair=="mf")and time==0):
        couple+=1
        time=1
    else:
        time=0 
print(f"only {couple} dog couples can be sold")
