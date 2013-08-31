#############################
# Created By: Sean Moriarty #
# Created On:1/29/13        #
# Last Edit: 1/29/13        #
#############################

#Total of numbers multiplied and that number reversed
total = 0
totalBackwards = 0

#Variable for largest palindrome
largestPalindrome = 0

#For all numbers inbetween a and b multiply by each other and then reverse and compare
for num in range(700,1000):
    for secondNum in range(700,1000):
        total = num * secondNum

        total = str(total)
        totalBackwards = total[::-1]
        totalBackwards = int(totalBackwards)
        total = int(total)

        #If number is palindrome and larger than currrent largest change to current largest
        if total == totalBackwards and total > largestPalindrome:
            largestPalindrome = total

print largestPalindrome
            



        
