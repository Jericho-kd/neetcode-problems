# 217. Contains Duplicate (easy)
def contains_duplicate(nums: list[int]) -> bool:
    s: set[int] = set()

    for el in nums:
        if el in s:
            return True
        s.add(el)

    return False


# 1. Two Sum (easy)
def two_sum(nums: list[int], target: int) -> list[int] | None:
    tmp: dict[int, int] = {}

    for idx, el in enumerate(nums):
        if target - el in tmp.keys():
            return [tmp[target-el], idx]
        tmp[el] = idx


# 242. Valid Anagram (easy)
def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    return sorted(s) == sorted(t)


# 49. Group Anagrams (medium)
def group_anagrams(strs: list[str]) -> list[list[str]]:  
    result: dict[tuple[int, ...], list[str]] = {}

    for word in strs:
        word_repr: list[int] = [0] * 26

        for el in word:
            word_repr[ord(el) - ord('a')] += 1 
        result.setdefault(tuple(word_repr), []).append(word)
    
    return list(result.values())


# 347. Top K Frequent (medium)
def top_k_frequent(nums: list[int], k: int) -> list[int]:
    tmp: dict[int, int] = {}
    result: list[int] = []

    for el in nums:
        tmp[el] = tmp.get(el, 0) + 1

    for _ in range(k):
        max_key = max(tmp, key=tmp.get)
        result.append(max_key)
        del tmp[max_key]

    return result

# Top K Frequent with Counter most_common solution
from collections import Counter

def top_k_frequent_counter(nums: list[int], k: int) -> list[int]:
    tmp = Counter(nums)

    return [key for key, value in tmp.most_common(k)]
    

def productExceptSelf(nums: list[int]) -> list[int]:
        result: list[int] = []
        for idx, el in enumerate(nums):
            if idx == 0:
                result.append(product([1], nums[idx+1:]))
            elif idx == len(nums) - 1:
                result.append(product(nums[0:idx], [1]))
            else:
                result.append(product(nums[0:idx], nums[idx+1:]))

        return result
                
    
def product(prefix: list[int], suffix: list[int]) -> int:
    pref_res, suff_res = 1, 1
    for el in prefix:
        pref_res *= el
    
    for el in suffix:
        suff_res *= el

    return pref_res * suff_res

print(productExceptSelf([1,2,3,4]))