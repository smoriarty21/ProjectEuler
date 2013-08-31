#############################
# Created By: Sean Moriarty #
# Created On:1/29/13        #
# Last Edit: 1/29/13        #
#############################

#List for numbers found divisable by 5 or 3
numbers = []

#variable for final sum
finalSum = 0

#Loop through all numbers
for num in range(1,1000):
    
    #Get remainder when divided by 3 and 5
    div3 = num % 3
    div5 = num % 5

    #If no remainder add to list of numbers divisable by 3 or 5
    if div3 == 0 or div5 == 0:
        numbers.append(num)

#Add all numbers in list together
for num in numbers:
    finalSum += num

#Show final sum
print finalSum
