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
    

# 238. Product of Array Except Self (medium)
def product_except_self(nums: list[int]) -> list[int]:
    result: list[int] = [1] * len(nums)
    prefix, postfix = 1, 1

    for i in range(len(nums)):
        result[i] = prefix
        prefix *= nums[i]

    for i in range(len(nums)-1, -1, -1):
        result[i] *= postfix
        postfix *= nums[i]

    return result


# 977. Squares of a Sorted Array (easy)
def array_of_squares(nums: list[int]) -> list[int]:
    if not nums:
        return []
    left, right = 0, len(nums) - 1
    result: list[int] = []

    while left < right:
        if abs(nums[left]) > abs(nums[right]):
            result.append(abs(nums[left])**2)
            left += 1
        elif abs(nums[left]) < abs(nums[right]):
            result.append(abs(nums[right])**2)
            right -= 1
        elif abs(nums[left]) == abs(nums[right]):
            result.append(abs(nums[left])**2)
            result.append(abs(nums[right])**2)
            left += 1
            right -= 1
    if left == right:
        result.append(abs(nums[left])**2)

    return result[::-1]


# 240. Search a 2D Matrix II (medium)
def search_matrix(matrix: list[list[int]], target: int) -> bool:
    m, n = 0, len(matrix[0]) - 1

    while m <= (len(matrix) - 1) and n >= 0:
        if target == matrix[m][n]:
            return True
        elif target < matrix[m][n]:
            n -= 1
        elif target > matrix[m][n]:
            m += 1

    return False
