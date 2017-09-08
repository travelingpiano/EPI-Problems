def look_and_say(n):
    #base case
    if n == 1:
        return '1'
    #inductive step
    prev_output = look_and_say(n-1)
    new_output = ""
    cur_num = prev_output[0]
    cur_count = 1
    for i in range(1,len(prev_output)):
        if prev_output[i] == cur_num:
            cur_count += 1
        else:
            new_output += str(cur_count) + cur_num
            cur_num = prev_output[i]
            cur_count = 1
    new_output += str(cur_count) + cur_num
    return new_output

print(look_and_say(3)) #expect 21
print(look_and_say(8)) #expect 1113213211
