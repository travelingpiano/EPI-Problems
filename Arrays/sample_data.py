import random
def sample_data(data,num):
    for i in range(num):
        rand_idx = random.randint(i,len(data)-1)
        data[i],data[rand_idx] = data[rand_idx], data[i]
    return data

print(sample_data([1,2,3,4,5],3))
