import random

def partition(arr,idx):
    pivot_el = arr[idx]
    # arr[idx] = None
    next_low = 0
    next_high = len(arr)-1
    #special case if length of array is less than or equal to one, just return the original array unmodified
    if len(arr) <= 1:
        return arr
    while next_high > next_low:
        #if low element is greater, move it to the top
        if arr[next_low] > pivot_el:
            arr[next_low],arr[next_high] = arr[next_high],arr[next_low]
            next_high -= 1
        #if low element is same as pivot, that means pivot element was placed too low; if pivot element placed too high, the previous comparison would have caught it
        elif arr[next_low] == pivot_el:
            arr[next_low],arr[next_low+1] = arr[next_low+1],arr[next_low]
        else:
            next_low += 1
    return arr

print(partition([1,3,2,4],2)) #expect [1,2,3,4]
array1 = list(range(15))
random.shuffle(array1)
print(array1)
print(array1[5])
print(partition(array1,5))
