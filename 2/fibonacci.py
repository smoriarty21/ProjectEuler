#############################
# Created By: Sean Moriarty #
# Created On:1/29/13        #
# Last Edit: 1/29/13        #
#############################

#Value for sum of two integers
sumValue = 0

#List for two numbers being added for fibonacci (I know this is a little out of the box but it works very well)
values = []

#List for all numbers in Fibonacci
fib = []

#List for even values to be added together
evenValues = []

#Value for sum of all even values
evenSum = 0

#Starting Values
values.append(0)
values.append(1)

#Max to count to
maxValue = 4000000

#While value is less than maxValue add to array
while sumValue <= maxValue:
    sumValue = (values[0] + values[1])
    fib.append(sumValue)
    values[0] = values[1]
    values[1] = sumValue
    
#Cut final number off if it goes over maxValue
if values[1] >= maxValue:
    fib.remove(values[1])

#Find even values and add to evenValues list
for num in fib:
    if num % 2 == 0:
        evenValues.append(num)

#Find sum of all values in evenValues list
for num in evenValues:
    evenSum += num

print evenSum

    
