from dataclasses import dataclass, field


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


# 11. Container With Most Water (medium)
def max_area(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    result = 0

    while left <= right:
        area = min(height[left], height[right]) * (right - left)
        result = max(result, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return result


# 1476. Subrectangle Queries (medium)
@dataclass
class SubrectangleQueries:
    rectangle: list[list[int]] = field(repr=True)

    def update_subrectangle(self, row1: int, col1: int, row2: int, 
                            col2: int, new_value: int) -> None:
        for r in range(row1, row2+1):
            for c in range(col1, col2+1):
                self.rectangle[r][c] = new_value

    def get_value(self, row: int, col: int) -> int:
        return self.rectangle[row][col]

# s = SubrectangleQueries([[1,2,1],[4,3,4],[3,2,1],[1,1,1]])
# s.get_value(0, 2)
# s.update_subrectangle(0, 0, 3, 2, 5)
# s.get_value(0, 2)
# s.get_value(3, 1)
# s.update_subrectangle(3, 0, 3, 2, 10)
# s.get_value(3, 1)
# s.get_value(0, 2)


# 13. Roman to Integer (easy)
def roman_to_int(s: str) -> int:
    roman_nums = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    result = 0

    s = s.replace('IV', 'IIII').replace('IX', 'VIIII')
    s = s.replace('XL', 'XXXX').replace('XC', 'LXXXX')
    s = s.replace('CD', 'CCCC').replace('CM', 'DCCCC')

    for char in s:
        result += roman_nums[char]

    return result


# 53. Maximum Subarray (medium)
def max_subarray(nums: list[int]) -> float:
    max_sum, current_sum = float('-inf'), 0

    for _, el in enumerate(nums):
        current_sum += el
        max_sum = max(max_sum, current_sum)
        current_sum = max(current_sum, 0)

    return max_sum
        

# 27. Remove Element (easy)
def remove_element(nums: list[int], val: int) -> int:
        result = 0

        for _, el in enumerate(nums):
            if el != val:
                nums[result] = el
                result += 1

        return result


# 128. Longest Consecutive Sequence (medium)
def longest_consecutive(nums: list[int]) -> int:
    result = 0
    num_set = set(nums)

    for num in nums:
        if (num - 1) not in num_set:
            length = 1

            while (num + length) in num_set:
                length += 1
            result = max(result, length)

    return result

