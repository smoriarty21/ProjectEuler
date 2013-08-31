#############################
# Created By: Sean Moriarty #
# Created On:1/31/13        #
# Last Edit: 2/02/13        #
#############################

def addPrimes(numPrimes):
    numPrimes = (numPrimes - 1)
    primesFound = 0
    primeChecking = 1
    primeSum = 0

    while primeChecking < numPrimes:
        primeChecking += 1
        
        if primeCheck(primeChecking) == True:
            primeSum += primeChecking
            primesFound += 1
            
    print primeSum
    



def primeCheck(n):
    n = abs(int(n))
    
    #0 and 1 are not prime
    if n < 2:
        return False

    #2 is only even prime number
    elif n == 2:
        return True

    #Eliminate all other even numbers
    elif n % 2 == 0:
        return False

    else:
        for x in range(3, int(n**0.5)+2, 2):
            if n % x == 0:
                return x, False
        return True


addPrimes(2000000)

    
        
    
