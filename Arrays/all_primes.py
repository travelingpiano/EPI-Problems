import math
import time
def all_primes(num):
    start_time = time.time()
    result = []
    for i in range(2,num):
        if check_prime(i,result):
            result.append(i)
    print(f"Took {time.time()-start_time}seconds")
    return result

def check_prime(num,cur_primes):
    idx = 0
    if len(cur_primes) == 0:
        return True
    while (cur_primes[idx] <= math.sqrt(num)):
        if num%cur_primes[idx] == 0:
            return False
        idx += 1
        if idx == len(cur_primes):
            return True
    return True

def optimized_primes(num):
    start_time = time.time()
    result = []
    is_prime = [False, False] + [True]*(num-1)
    for i in range(2,num):
        if is_prime[i]:
            result.append(i)
            for j in range(i,num,i):
                is_prime[j] = False
    print(f"Took {time.time()-start_time}seconds")
    return result

print(all_primes(18)) #expect [2,3,5,7,11,13,17]
print(optimized_primes(18)) #expect [2,3,5,7,11,13,17]
