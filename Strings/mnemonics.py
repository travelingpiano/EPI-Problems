MAPPING = ['0','1','ABC','DEF','GHI','JKL','PQRS','TUV','WXYZ']
def mnemonics(input_digits):
    possible_combi = list(MAPPING[int(input_digits[-1])])
    if len(input_digits) == 1:
        return possible_combi
    prev_output = mnemonics(input_digits[:-1])
    new_output = []
    for i in prev_output:
        for j in possible_combi:
            new_output.append(i+j)
    return new_output

print(mnemonics("12")) #expect ['1A','1B','1C']
