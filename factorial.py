def recursiveFact (num) :
    return num * recursiveFact(num-1) if num > 1 else 1;

def iterativeFact (num) :
    if num < 0 :
        return 0
    elif num == 0 or num ==1 :
        return 1
    else :
        fact =1
        while (num>1) :
            fact  = fact * num
            num =num-1
            return fact

import math
def inbuildFact (num) :
    return(math.factorial(num))

if __name__ == '__main__' :
    number= int (input ("Enter a number:"))
    type=input ("Enter type of function [Recursive , Iterative , Inbuild]")
    if type == "Recursive" :
        recursiveFact(number)
    elif type == "Iterative" :
        iterativeFact(number)
    else :
        inbuildFact(number)




