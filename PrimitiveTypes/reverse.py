import math
def reverse(x):
    #to take into account negative numbers
    negative = False
    if x < 0:
        negative = ~negative
        x = -x
    remainder = x
    reversed_x = 0
    while remainder > 0:
        reversed_x, remainder = reversed_x*10 + remainder%10, math.floor(remainder/10)
    if negative:
        reversed_x = -reversed_x
    return reversed_x

print(reverse(-104))
