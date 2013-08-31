#############################
# Created By: Sean Moriarty #
# Created On:1/29/13        #
# Last Edit: 1/29/13        #
#############################

#Variable for sum of square and square of sum
sumSquare = 0
squareSums = 0

number = 0
square = 0

#Get sum square
for num in range(1,101):
    square = num * num
    sumSquare += square

#Get square sum
for num in range(1,101):
    number += num

squareSums = number * number

print squareSums - sumSquare



