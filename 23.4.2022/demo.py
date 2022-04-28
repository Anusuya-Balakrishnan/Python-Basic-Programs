import re
##a="Hello1 how are you? 1236e re3"
##match=re.findall("[A-Za-z0-9]{3}",a)
##print(match)

##a="123145517895 "
##match=re.search("[\d]{12}",a)
##print(match.group()==a)
##s=str(match.group())
##data=' '.join(re.findall("[\d]{4}",s))
##print(data)

##strvalue="BFDAP1245R  is a value  BFDAP1245R"
##
##pattern="[A-Z]{5}[\d]{4}[A-Z]"
##match=re.findall(pattern,strvalue)
##print(match)

strvalue="http://www.programiz.com/python-programming/regex"
pattern="^[a-z]+:[/]{2}\S[^:]"

match=re.search(pattern,strvalue)
print(match.string)
