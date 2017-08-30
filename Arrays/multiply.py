def multiply(num1,num2):
    #we'll multiply the entire num1 with every digit of num2 one by one
    result = []
    for idx_2 in range(len(num2)):
        sub_result = []
        if num2[idx_2] != 0:
            for idx_1 in range(len(num1)):
                if num1[idx_1] != 0:
                    multipled_result = num2[idx_2]*num1[idx_1]
                    multipled_set = []
                    if multipled_result >= 10:
                        multipled_set = [multipled_result//10,multipled_result%10]
                    else:
                        multipled_set = [multipled_result]
                    multipled_set += [0]*(len(num1)-1-idx_1)
                    if idx_1 == 0:
                        sub_result = multipled_set
                    else:
                        sub_result = sum_two_arrays(sub_result,multipled_set)
        if idx_2 == 0:
            result = sub_result + [0]*(len(num2)-1-idx_2)
        else:
            result = sum_two_arrays(result,sub_result + [0]*(len(num2)-1-idx_2))
    return result

#array for num1 always longer or equal to array for num2
def sum_two_arrays(num1,num2):
    carry = 0
    for sub_idx in range(len(num2)):
        if carry + num2[-1-sub_idx] + num1[-1-sub_idx] < 10:
            num1[-1-sub_idx] += carry + num2[-1-sub_idx]
            carry = 0
        else:
            num1[-1-sub_idx] = (num2[-1-sub_idx]+num1[-1-sub_idx]+carry)%10
            carry = 1
    if carry == 1:
        if (len(num1)==len(num2)):
            num1 = [1] + num1
        else:
            num1[-1-len(num2)] += 1
    return num1

print(multiply([2,3],[5])) #expect [1,1,5]
print(multiply([2,2],[4,4])) #expect [9,6,8]
print(multiply([3,7],[7,3])) #expect [2,7,0,1]
print(multiply([3,5,7,4],[2,9,7])) #expect [1,0,6,1,4,7,8]
