class LastDigitChecker:
    def isValid(self,number):
        self.number=number
        if(self.number>=10 and self.number<=1000):
            return True
        else:
            return False
    def hasSameLastDigit(s,number1,number2,number3):
        s.number1=int(number1)
        s.number2=int(number2)
        s.number3=int(number3)
        if(s.isValid(s.number1)and s.isValid(s.number2) and s.isValid(s.number3)):
            s.last1=int(s.number1%10)
            s.last2=int(s.number2%10)
            s.last3=int(s.number3%10)
            if((s.last1==s.last2)or(s.last1==s.last3)or(s.last2==s.last3)):
                return True
            else:
                return False
        else:
            return "Invalid value"

last=LastDigitChecker()
print("hasSameLastDigit(41,22,71) :",last.hasSameLastDigit(41,22,71))
print("hasSameLastDigit(23,32,42)",last.hasSameLastDigit(23,32,42))
print("hasSameLastDigit(9,99,999)",last.hasSameLastDigit(9,99,999))

            
                
           
              
           
