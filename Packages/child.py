from Packages.parent.Parent import add,sub 
class Child:
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        if(b!=0):
            return a/b
        else:
            return 0

c=Child()
print(add(2,3))
print(sub(2,3))
print(c.mul(2,3))
print(c.div(2,3))
    
