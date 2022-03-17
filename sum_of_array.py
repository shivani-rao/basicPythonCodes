def array_sum (arr) :
    sum=0
    for i in arr:
        sum = sum+i
    return sum


if __name__ == '__main__' :
    arr = []
    num = int (input("Enter size of array :"))
    print ("Enter elements of array : ")
    for i in range (0,num) :
        ele = int(input())
        arr.append(ele)
    print ("sum of array elements :",array_sum(arr))



