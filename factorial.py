def recursiveFact (num) :
    return num * recursiveFact(num-1) if num > 1 else 1

def iterativeFact (n) :
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num

import math
def inbuildFact (num) :
    return(math.factorial(num))

if __name__ == '__main__' :
    number= int (input ("Enter a number:"))
    type=input ("Enter type of function [Recursive , Iterative , Inbuild]")
    if type == "Recursive" :
       print("Result of recursiveFact function is ",recursiveFact(number))
    elif type == "Iterative" :
        print("Result of iterativeFact function is ",iterativeFact(number))
    else :
       print("Result of inbuildFact function is ",inbuildFact(number))






