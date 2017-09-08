def roman_dec_conversion(roman_str):
    conversion_hash = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result_int = 0
    prev_num = conversion_hash[roman_str[0]]
    for i in roman_str:
        if prev_num < conversion_hash[i]:
            result_int -= 2*prev_num
        result_int += conversion_hash[i]
        prev_num = conversion_hash[i]
    return result_int
    
print(roman_dec_conversion('XXIII')) #expect 23
print(roman_dec_conversion('LIX')) #expect 59
