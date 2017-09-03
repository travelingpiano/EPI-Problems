import random
def random_subset(arr, subset_size):
    for i in range(subset_size):
        idx = random.randint(i,len(arr)-1)
        arr[i],arr[idx] = arr[idx], arr[i]
    return arr[0:subset_size]

def subset_n(n,subset_size):
    changed_vals = {}
    for i in range(subset_size):
        to_occupy = random.randrange(0,n)
        cur_value = changed_vals.get(i,i)
        new_value = changed_vals.get(to_occupy,to_occupy)
        changed_vals[to_occupy] = cur_value
        changed_vals[i] = new_value
    return [changed_vals[i] for i in range(subset_size)]

print(random_subset([1,2,3],2))
print(subset_n(3,2))
