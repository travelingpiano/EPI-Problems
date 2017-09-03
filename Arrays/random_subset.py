import random
def random_subset(arr, subset_size):
    for i in range(subset_size):
        idx = random.randint(i,len(arr)-1)
        arr[i],arr[idx] = arr[idx], arr[i]
    return arr[0:subset_size]

print(random_subset([1,2,3],2))
