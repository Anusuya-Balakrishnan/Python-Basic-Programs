def longestCommonPrefix(strs):
    prefix=""
    val=""
    for i in range((len(strs)-2)):
        for j in strs[i]:
            if(prefix==""):
                if(j in strs[i+1]):
                    prefix+=j
                    print(prefix)
            else:
                if j in prefix:
                    val+=j
                    print(val)          
    return prefix
                    
print(longestCommonPrefix(["flower","flow","flight"]))
