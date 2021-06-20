

def bin_search(arr, low, high, q, target):
    mid = 0
    mid = (int)(((high - low)/2) + low)

    
    if(high < low):
        return -1
       
    
    if((target - q) == arr[mid]):
        return mid
    
    if(arr[mid] + q > target):
        return bin_search(arr, low, mid - 1, q, target)
    else:
        return bin_search(arr, mid + 1, high, q, target)


def sum_target(arr, target):
    l1 = sorted(arr)

    if len(arr) > 2:
        for i in range(len(arr)):
            print
            b = bin_search(l1, i, len(arr) -1, l1[i], target)
            if b > -1:
                return [l1[i], l1[b]]
        return [0]
    else:
        if(len(l1) == 2):
            if(l1[0] + l1[1] == target):
                return [l1[0], l1[1]]
            else:
                return [0]
        else:
            return [0]


 

assert(sum(sum_target([10, 15, 3, 7], 10)) == 10)
assert(sum(sum_target([10, 15, 3, 7], 17)) == 17)
assert(sum(sum_target([10, 15, 3, 7], 99)) == 0)
assert(sum(sum_target([3, 7], 99)) == 0)
assert(sum(sum_target([3, 7], 10)) == 10)
assert(sum(sum_target([7], 10)) == 0)
assert(sum(sum_target([10, 15, 3, 7], 18)) == 18)
assert(sum(sum_target([10, 15, 3, 7], 25)) == 25)
