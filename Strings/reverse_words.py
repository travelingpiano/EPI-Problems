def reverse_words(sentence):
    sentence_list = sentence.split(' ')
    output_list = []
    for word in sentence_list:
        output_list = [word] + output_list
    return " ".join(output_list)

print(reverse_words("Bob likes Alice")) #expect "Alice likes Bob"
