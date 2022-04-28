class Printer:
    
    def __init__(self,tonerLevel, duplex):
        if(tonerLevel>-1 and tonerLevel<=100):
            
            self.__tonerLevel=tonerLevel
        else:
            self.__tonerLevel=-1
            
        self.__pagesPrinted=0
        self.__duplex=duplex
        
    def addToner(self, tonerAmount):
        if(tonerAmount>0 and tonerAmount<=100):
            if(self.__tonerLevel+tonerAmount>100):
                return -1
            else:
                self.tonerAmount=tonerAmount
                
        self.__tonerLevel=+self.tonerAmount
        
        return (int)(self.__tonerLevel)

        
    def printPages(self,pages):
        
        self.pagesToPrint=pages
        
        if(self.__duplex):
            
            self.pagesToPrint=(pages/2)+(pages%2)
            
        self.__pagesPrinted+=self.pagesToPrint
        
        return (int)(self.__pagesPrinted)
    
    def getPagesPrinted(self):
        return (int)(self.__pagesPrinted)

printer=Printer(50,True)
print(printer.addToner(50))
print("initial pages count",printer.getPagesPrinted())
pagesPrinted=printer.printPages(4)
print("Pages printed was",pagesPrinted,"new total count for printer = ",printer.getPagesPrinted())
pagesPrinted=printer.printPages(2)
print("Pages printed was",pagesPrinted,"new total count for printer = ",printer.getPagesPrinted())
