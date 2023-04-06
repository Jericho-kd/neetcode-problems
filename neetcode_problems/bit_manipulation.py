# 136. Single Number (easy)
def single_number(nums: list[int]) -> int:
    result = 0

    for el in nums:
        result ^= el
        
    return result


# 191. Number of 1 Bits (easy)
def hamming_weight(n: int) -> int:
    count = 0

    while n:
        if n & 1 == 1:
            count += 1
        n >>= 1
    
    return count