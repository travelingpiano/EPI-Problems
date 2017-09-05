import functools, string
def base_conversion(input_str, input_b, output_b):
    #convert to base 10 integer
    input_int = functools.reduce(lambda accum, el: accum*int(input_b)+string.digits.index(el),input_str,0)
    #convert to new output base
    numbers = string.digits + "ABCDEF"
    output_list = []
    while input_int > 0:
        output_list.append(numbers[input_int%output_b])
        input_int //= output_b
    output_list.reverse()
    return "".join(output_list)

print(base_conversion("23",4,2)) #expect "1011"
print(base_conversion("615",7,13)) #expect "1A7"
