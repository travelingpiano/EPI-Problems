def swap_bit(num,i,j):
    if ((num>>i) & 1) != ((num>>j)&1):
        bit_mask = (1<<i) | (1<<j)
        num ^= bit_mask
    return num

print(swap_bit(8,3,0))
