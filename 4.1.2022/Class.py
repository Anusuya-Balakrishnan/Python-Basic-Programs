"""even digit sum
/*Write a method named getEvenDigitSum with one parameter of type int called number.

The method should return the sum of the even digits within the number.

If the number is negative, the method should return -1 to indicate an invalid value.


EXAMPLE INPUT/OUTPUT:

* getEvenDigitSum(123456789); → should return 20 since 2 + 4 + 6 + 8 = 20

* getEvenDigitSum(252); → should return 4 since 2 + 2 = 4

* getEvenDigitSum(-22); → should return -1 since the number is negative


NOTE: The method getEvenDigitSum should be defined as public static like we have been doing so far in the course.

NOTE: Do not add a main method to the solution code.
*/"""
class EvenDigitSum:
    def __init__(self, number):
        self.number=int(number)
        self.number1=int(number)
        self.rem=0
        self.sum=0
        while(self.number>0):
            self.rem=int(self.number%10)
            self.number=int(self.number/10)
            print(self.number)
            if(self.rem%2==0):5rf
                self.sum+=self.rem
        print("Sum of Even Digit of ",self.number1 ," is :",self.sum)
          
even=EvenDigitSum(252)
even=EvenDigitSum(2000)
even=EvenDigitSum(123456789)




















            
