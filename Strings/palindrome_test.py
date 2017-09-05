import re
def palindrome_test(input_str):
    #first, strip string of non-alphanumeric characters
    input_str = re.sub('\W+','',input_str).lower()
    for i in range(len(input_str)//2):
        if input_str[i] != input_str[-i-1]:
            return False
    return True

print(palindrome_test("A man, a plan, a canal, Panama.")) #expect True
print(palindrome_test("Able was I, ere I saw Elba!")) #expect True
print(palindrome_test("Ray a Ray")) #expect False
