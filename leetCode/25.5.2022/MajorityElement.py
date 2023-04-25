##Given an array nums of size n, return the majority element.
##
##The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
##
## 
##
##Example 1:
##
##Input: nums = [3,2,3]
##Output: 3
##Example 2:
##
##Input: nums = [2,2,1,1,1,2,2]
##Output: 2

def majorityElement(nums):
        inputSet=set(nums)
        inputDict={}
        print("set is ",inputSet)
        temp=0
        tempKey=0
        for i in inputSet:
            count=nums.count(i)
            if(temp<count):
                    temp=count
                    tempKey=i
        return tempKey
        
##        modifyList=list(inputDict.items())
##        valueList=list(inputDict.values())
##        print( modifyList,max(valueList))
##        for i in range(len(modifyList)):
##            for j in range(i+1,len(modifyList)):
##                if(maxValue[1]<modifyList[j][1]):
##                    maxValue=modifyList[j]
##                    print("final",maxValue)
##        return maxValue[0]
print(majorityElement([9,9,9,2,2,5,6,6,7,8,8]))



























































