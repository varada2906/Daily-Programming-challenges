import math
def primeFactors(n):
    # Print the number of two's that divide n
    while n % 2 == 0:
        print (2,end=' ')
        n = n / 2
        
#for odd
    for i in range(3, int(math.sqrt(n))+1, 2):
        
        
        while n % i == 0:
            print (i,end=' ')
            n = n / i
            
   #for number greater than 21
    if n > 2:
        print (n,end=' ')
        

n = 18
primeFactors(n)


