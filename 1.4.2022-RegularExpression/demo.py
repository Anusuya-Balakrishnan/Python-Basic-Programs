"""import re
a=input("enter a string: ")
#pattern=re.compile("(b*)$")
value=re.findall("(\w+)(b*)$",a)
print("match found",value)"""

"[a-z]+[A-Z]+(\_\-)?(\d)*"
import re
a=input("enter a variable name:")
pattern =re.compile(r"^[A-Za-z\_]+(\d*)+[^\W]")
value=pattern.search(a)
if(value):
    print("Valid variable is ",value.group())
else:
    print("invalid variable")
