
##inputSet=set(nums)
##inputDict={}
##for i in inputSet:
##    count=nums.count(i)
##    inputDict[i]=count
##modifyList=list(inputDict.items())
##print(modifyList)
##maxValue=modifyList[0][1]
##for i in range(len(modifyList)):
##    for j in range(i+1,len(modifyList)):
##        if(modifyList[i][1]<modifyList[j][1]):
##            maxValue=modifyList[j]
##return maxValue[0]
##
def majorityElement(nums):
        inputSet=set(nums)
        inputDict={}
        print("set is ",inputSet)
        for i in inputSet:
            count=nums.count(i)
            inputDict[i]=count
        modifyList=list(inputDict.items())
        print(modifyList)
        maxValue=modifyList[0]
        print("initial",maxValue)
        for i in range(len(modifyList)):
            for j in range(i+1,len(modifyList)):
                if(maxValue[1]<modifyList[j][1]):
                    maxValue=modifyList[j]
                    print("final",maxValue)
        return maxValue[0]
print(majorityElement([9,9,9,2,2,5,6,6,7,8,8]))



























































