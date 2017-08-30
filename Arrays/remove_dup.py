def remove_dup(arr):
    cur_el = arr[0]
    idx = 1
    while idx < len(arr):
        if arr[idx] == cur_el:
            arr[idx] = 0
        else:
            cur_el = arr[idx]
        idx += 1
    idx = 1
    first_zero = 0
    while idx < len(arr):
        if (arr[idx] == 0) & (first_zero == 0):
            first_zero = idx
        elif (arr[idx] != 0) & (first_zero > 0):
            arr[idx], arr[first_zero] = arr[first_zero],arr[idx]
            first_zero += 1
        idx += 1
    print(arr)
    #no duplicates
    return first_zero

print(remove_dup([1,2,2,3,3])) #expect [1,2,3,0,0]
print(remove_dup([1,2,3,4])) #expect [1,2,3,4]
print(remove_dup([1,1,1,1])) #expect [1,0,0,0]
print(remove_dup([1,2,2,2,2,3,3,4,4,4])) #expect [1,2,3,4,0,0,0,0,0,0]
