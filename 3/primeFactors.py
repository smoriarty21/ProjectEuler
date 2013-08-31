#############################
# Created By: Sean Moriarty #
# Created On:1/29/13        #
# Last Edit: 1/29/13        #
#############################

#List of found prime factors
primeFactors = []

#Variable for largets of all prime factors
largestPrime = 0

#Variable you are checking for prime factors of
prime = 600851475143
done = 0
numChecking = 2

while done == 0:
    if prime % numChecking == 0:
        primeFactors.append(numChecking)
        
    numChecking += 1

    if numChecking >= (prime / 100000):
        done = 1

#Remove all values divisable by beggining numbers
length = len(primeFactors)
start = 0

for num in primeFactors:
    for factor in primeFactors:
        if factor != num and factor % num == 0:
            primeFactors.remove(factor)

#Second run through to remove last factor(bug needs fixin)
for num in primeFactors:
    for factor in primeFactors:
        if factor != num and factor % num == 0:
            primeFactors.remove(factor)

for num in primeFactors:
    if num > largestPrime:
        largestPrime = num


print primeFactors

