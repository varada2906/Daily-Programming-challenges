import math
def countDivisors(n):
    count=0
    #iterate from 1 to the square root of N
    for i in range(1,(int)(math.sqrt(n))+1):  
        if (n/i== i):#check if i is divisor of n
            count=count+1#if divisor equal count 1 else 2
        else:
            count=count+2
    return count
print("Total divisors are:",countDivisors(12))
#Output:6 ,The program outputs 6,as the divisors of 12 are 1,2,3,4,6,12
