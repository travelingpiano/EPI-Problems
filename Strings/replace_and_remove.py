def replace_and_remove(input_list):
    output_list = []
    for el in input_list:
        if el == "a":
            output_list.append("d")
            output_list.append("d")
        elif el != "b":
            output_list.append(el)
    return output_list

# def eff_randr(input_list):
#     write_idx = 0
#     for i in input_list:
#         if i == "a":
#             write_idx += 2


print(replace_and_remove(["d","b","c","a"])) #expect ["d","c","d","d"]
