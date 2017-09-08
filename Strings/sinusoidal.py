def sinusoidal(input_str):
    top_substr = ""
    middle_substr = ""
    bottom_substr = ""
    for i in range(len(input_str)):
        if i%2 == 0:
            middle_substr += input_str[i]
        elif (i-1)%4 == 0:
            top_substr += input_str[i]
        else:
            bottom_substr += input_str[i]
    return top_substr + middle_substr + bottom_substr
print(sinusoidal('Hello World!')) #expect 'e lHloWrdlo!'
