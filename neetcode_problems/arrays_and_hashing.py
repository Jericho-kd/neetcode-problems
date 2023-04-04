#217. Contains Duplicate
def contains_duplicate(nums: list[int]) -> bool:
    s: set[int] = set()

    for el in nums:
        if el in s:
            return True
        s.add(el)

    return False


#1. Two Sum
def two_sum(nums: list[int], target: int) -> list[int] | None:
    tmp: dict[int, int] = {}

    for idx, el in enumerate(nums):
        if target - el in tmp.keys():
            return [tmp[target-el], idx]
        tmp[el] = idx


#242. Valid Anagram
def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    return sorted(s) == sorted(t)
