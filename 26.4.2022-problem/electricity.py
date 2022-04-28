class ElectricityBill:
    def __init__(self, custId,name,date,month,unit):
        self.custId=custId
        self.name=name
        self.date=date
        self.month=month
        self.unit=unit
        self.amount=lambda x: x*10 if(x>1 and x<100) else (x*15 if(x>=100 and x<200)
                    else( x*20 if(x>=200 and x<300) else ( x*25 if(x>=300) else 0)))
        print("Electricity Amount : ",self.amount(unit))
                    

e=ElectricityBill(12,"aaa","26.4.2022","april",65)


        
        
