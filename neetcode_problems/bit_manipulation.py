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


# 338. Counting Bits (easy)
def count_bits(n: int) -> list[int]:
    result: list[int] = []

    for num in range(n+1):
        count: int = 0

        while num != 0:
            if num & 1 == 1:
                count += 1
            num >>= 1
        result.append(count)

    return result


#190. Reverse Bits (easy)
def reverse_bits(n: int) -> int:
    reversed_num: int = 0

    for _ in range(32):
        reversed_num <<= 1
        reversed_num |=  (n & 1)
        n >>= 1

    return reversed_num
