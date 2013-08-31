#############################
# Created By: Sean Moriarty #
# Created On:1/31/13        #
# Last Edit: 1/31/13        #
#############################

found = False

while found == False:
    for a in range(1,900):
        for b in range(1,900):
            for c in range(1,900):
                if (a * a) + (b * b) == (c * c):
                    if (a + b + c) == 1000 :
                        print a * b * c
                        found = True
                    
