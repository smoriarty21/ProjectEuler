#############################
# Created By: Sean Moriarty #
# Created On:1/29/13        #
# Last Edit: 1/29/13        #
#############################

#Starting number for smallest multiple
multiple = 232000000

#Variable to stop when found
found = 0

#Variable for number of numbers found with no remainder and remainder value
noRem = 0
remainder = 0

#While not found loop
while found == 0:
    #For number 1 - 20
    for num in range(1,21):
        #Find remainder between numbers
        remainder = multiple % num

        #if no remainder add one to noRem
        if remainder == 0:
            noRem += 1

        #On last number check for being divisable by all and if it is show it
        if num == 20:
            if noRem == 20:
                found = 1
                print multiple
                noRem = 0

            #Reset noRem    
            noRem = 0
            
    #Add one to multiple and do it again
    multiple += 1
