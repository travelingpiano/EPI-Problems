def my_int(input_str):
    result = 0
    negative = False
    numbers = "0123456789"
    if input_str[0] == "-":
        negative = True
        input_str = input_str[1:]
    for i in range(len(input_str)):
        result = result*10 + numbers.index(input_str[i])
    if negative:
        return -result
    else:
        return result

print(my_int("123")) #expect 123
print(my_int("-2516")) #expect -2516
