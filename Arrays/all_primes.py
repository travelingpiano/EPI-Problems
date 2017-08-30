import math
def all_primes(num):
    result = []
    for i in range(2,num):
        if check_prime(i,result):
            result.append(i)
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

print(all_primes(18)) #expect [2,3,5,7,11,13,17]
