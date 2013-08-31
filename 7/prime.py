#############################
# Created By: Sean Moriarty #
# Created On:1/29/13        #
# Last Edit: 1/29/13        #
#############################

prime = True
primeFound = 0

for num in range(2,2000000):
    if num == 2:
        primeFound += 1
    else:
        for div in range(2,num):
            if (num % div) == 0:
                prime = False
                break
                

        if prime == True:
            primeFound += 1
            print num
            print primeFound
            print "\n"
        else:
            prime = True

    if primeFound == 10001:
        #print num
        break
