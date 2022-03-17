def sum (num1 ,num2) :
    total = int(num1) + int(num2)
    print("The sum of {0} and {1} is {2}".format(num1,num2,total))

if __name__ == '__main__' :
    number1 = input("First number: ")
    number2 = input("\nSecond number: ")
    sum(number1,number2) ;
