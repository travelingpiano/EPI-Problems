import math
def palindrome(num):
    #return all negative numbers as false
    if num < 0:
        return False
    num_digits = math.ceil(math.log10(num))
    mask = 10**(num_digits-1)
    for i in range(num_digits//2):
        if num//mask != num%10:
            return False
        num = (num%mask)//10
        mask //= 100
    return True

print(palindrome(12321))
print(palindrome(1241))
print(palindrome(1))
