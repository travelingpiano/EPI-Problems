#x being double, y being integer, return x**y
#can take in both negative and positive y
def power_x_y(x,y):
    if y == 0:
        return 1
    if y < 0:
        y = -y
        x = 1/x
    power = y
    result = x
    while power > 1:
        result = result*result
        if power & 1: #power is odd
            result *= x
        power >>= 1
    return result

print(power_x_y(2,-5))
