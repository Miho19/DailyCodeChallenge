def maxsum(arr):
    sum1 = arr[0]
    sum2 = 0
    new_sum = 0

    for i in range(len(arr)):
        new_sum = max(sum1, sum2)
        sum1 = sum2 + arr[i]
        sum2 = new_sum
    
    return max(sum1, sum2)








# result = 13
maxsum([2, 4, 6, 2, 5])

# result = 10
maxsum([5, 1, 1, 5])
