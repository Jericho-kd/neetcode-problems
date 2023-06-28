import neetcode_problems.arrays_and_hashing as ah_problems
import tests


@tests.pytest.mark.parametrize("nums, result", 
                               [([1,2,3,1], True),
                                ([1,2,3,4], False),
                                ([1,1,1,3,3,4,3,2,4,2], True)])
def test_contains_duplicate(nums: list[int], result: bool):
    assert ah_problems.contains_duplicate(nums) == result


@tests.pytest.mark.parametrize("nums, target, result", 
                               [([2,7,11,15], 9, [0, 1]),
                                ([3,2,4], 6, [1, 2]),
                                ([3, 3], 6, [0, 1])])
def test_two_sum(nums: list[int], target: int, result: list[int] | None):
    assert ah_problems.two_sum(nums, target) == result


@tests.pytest.mark.parametrize("s, t, result", 
                               [("anagram", "nagaram", True),
                                ("cat", "rat",  False)])
def test_is_anagram(s: str, t: str, result: bool):
    assert ah_problems.is_anagram(s, t) == result


@tests.pytest.mark.parametrize("strs, result",
                               [(["eat","tea","tan","ate","nat","bat"], [["eat","tea","ate"],["tan","nat"],["bat"]]),
                                (["a"], [["a"]])])
def test_group_anagrams(strs: list[str], result: list[list[str]]):
    assert ah_problems.group_anagrams(strs) == result


def test_top_k_frequent():
    assert ah_problems.top_k_frequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]
    assert ah_problems.top_k_frequent([1], 1) == [1]


def test_top_k_frequent_counter():
    assert ah_problems.top_k_frequent_counter([1, 1, 1, 2, 2, 3], 2) == [1, 2]
    assert ah_problems.top_k_frequent_counter([1], 1) == [1]


def test_product_except_self():
    assert ah_problems.product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert ah_problems.product_except_self([-1,1,0,-3,3]) == [0,0,9,0,0]


def test_array_of_squares():
    assert ah_problems.array_of_squares([-6, -5, -4, -3, -2, 1, 2, 3, 4]) == [1, 4, 4, 9, 9, 16, 16, 25, 36]
    assert ah_problems.array_of_squares([-10000, -9999, -7, -5, 0, 0, 10000]) == [0, 0, 25, 49, 99980001, 100000000, 100000000]
    assert ah_problems.array_of_squares([]) == []


def test_search_matrix():
    assert ah_problems.search_matrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20) == False
    assert ah_problems.search_matrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5) == True


def test_max_area():
    assert ah_problems.max_area([1,8,6,2,5,4,8,3,7]) == 49
    assert ah_problems.max_area([1, 1]) == 1


def test_roman_to_int():
    assert ah_problems.roman_to_int("III") == 3
    assert ah_problems.roman_to_int("LVIII") == 58
    assert ah_problems.roman_to_int("MCMXCIV") == 1994


def test_max_subarray():
    assert ah_problems.max_subarray([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert ah_problems.max_subarray([5,4,-1,7,8]) == 23
    assert ah_problems.max_subarray([-1, -1, -1, -2]) == -1


def test_remove_element():
    assert ah_problems.remove_element([3,2,2,3], 3) == 2
    assert ah_problems.remove_element([0,1,2,2,3,0,4,2], 2) == 5


def test_longest_consecutive():
    assert ah_problems.longest_consecutive([100,4,200,1,3,2]) == 4
    assert ah_problems.longest_consecutive([0,3,7,2,5,8,4,6,0,1]) == 9
