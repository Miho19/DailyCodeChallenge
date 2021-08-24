


def digitSum(num: int):
    sum = 0
    digit = 0

    while num > 0:
        digit = (int)(num) % 10
        sum += digit
        num /= 10
    return sum

def perfectSum(start: int):
    ret = 0
    number = start
    while 1:
        ret = digitSum(number)
        if(ret == 10):
            return number
        number += 1 
    

def nperfectSum(n: int):
    ret = 0
    num = 18
    while n >= 1:
        ret = perfectSum(num + 1)
        n -= 1
        num = ret
    return num


print(nperfectSum(1))
print(nperfectSum(2))
print(nperfectSum(3))
