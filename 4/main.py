# o(n) time, constant space


def positive(arr):
    arr.sort()

    for x in range(len(arr) - 1):
        if(arr[x + 1] != arr[x] + 1 and arr[x] > -1):
            return arr[x] + 1
    return arr[-1] + 1


assert(positive([3, 4, -1, 1]) == 2) 

assert(positive([1, 2, 0]) == 3)

assert(positive([-4, -10, 100, 5, 6, -1, 0]) == 1)

assert(positive([ 2, 3, -7, 6, 8, 1, -10, 15 ]) == 4)

assert(positive([1, 1, 0, -1, -2]) == 2)