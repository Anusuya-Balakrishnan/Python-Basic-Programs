"""    /*
 Write a method named getGreatestCommonDivisor with two parameters of type int named first and second. 

If one of the parameters is &lt; 10, the method should return -1 to indicate an invalid value.

The method should return the greatest common divisor of the two numbers (int).

The greatest common divisor is the largest positive integer that can fully divide each of the integers (i.e. without leaving a remainder).


For example 12 and 30:

12 can be divided by 1, 2, 3, 4, 6, 12

30 can be divided by 1, 2, 3, 5, 6, 10, 15, 30

The greatest common divisor is 6 since both 12 and 30 can be divided by 6, and there is no resulting remainder.


EXAMPLE INPUT/OUTPUT:

* getGreatestCommonDivisor(25, 15); should return 5 since both can be divided by 5 without a remainder

* getGreatestCommonDivisor(12, 30); should return 6 since both can be divided by 6 without a remainder

* getGreatestCommonDivisor(9, 18); should return -1 since the first parameter is &lt; 10

* getGreatestCommonDivisor(81, 153); should return 9 since both can be divided by 9 without a remainder


HINT: Use a while or a for loop and check if both numbers can be divided without a remainder.

HINT: Find the minimum of the two numbers.


NOTE: The method getGreatestCommonDivisor should be defined as public static like we have been doing so far in the course.

NOTE: Do not add a main method to the solution code."""
class GreatestCommonDivisor:
    def getGreatestCommonDivisor(s,number1,number2):
        s.number1=number1
        s.number2=number2
        s.greatest=0
        if(s.number1<10 or s.number2<10):
            return "Invalid Value"
        else:
            if(s.number1>s.number2):
                for i in range(1,s.number2+1):
                    if(s.number1%i==0 and s.number2%i==0):
                        s.greatest=i
            elif(s.number2>s.number1):
                for i in range(1,s.number1+1):
                    if(s.number1%i==0 and s.number2%i==0):
                        s.greatest=i

            return s.greatest

g=GreatestCommonDivisor()
print("Greatest Common Divisor",g.getGreatestCommonDivisor(25,15))
print("Greatest Common Divisor",g.getGreatestCommonDivisor(12,30))
print("Greatest Common Divisor",g.getGreatestCommonDivisor(9,18))
print("Greatest Common Divisor",g.getGreatestCommonDivisor(81,153))




















