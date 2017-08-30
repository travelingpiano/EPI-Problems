def plus_one(arr):
    #start from the smallest, or rightmost digit
    cur_idx = len(arr)-1
    while cur_idx > 0:
        if arr[cur_idx] + 1 < 10:
            arr[cur_idx] += 1
            return arr
        #if need to carry
        else:
            arr[cur_idx] = 0
            cur_idx -= 1
    #if largest element needs to carry (i.e. we need to shift a '1' in the front)
    if arr[cur_idx] + 1 < 10:
        arr[cur_idx] += 1
        return arr
    else:
        arr[cur_idx] = 0
        return [1] + arr

print(plus_one([1,2,9])) #expect [1,3,0]
print(plus_one([9,9])) #expect [1,0,0]
