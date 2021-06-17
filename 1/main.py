#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17
# target = a + b
# target - a = b



def bin_search(arr, low, high, q, target):
    mid = 0
    mid = (int)(((high - low)/2) + low)

    
    if(high < low):
        return -1    
    
    if((target - q) == arr[mid]):
        
        return arr[mid]
    if((target - q) > arr[mid]):
        return bin_search(arr, low, mid - 1, q, target)
    else:
        return bin_search(arr, mid + 1, high, q, target)


def sum_target(arr, target):
    if len(arr) > 2:
        l1 = sorted(arr)
        for i in range(len(arr)):
            print
            b = bin_search(l1, i, len(arr) -1, l1[i], target)
            if b > -1:
                print(target, " = " , b , " + ", l1[i])
                break
 


sum_target([10, 15, 3, 7], 10)