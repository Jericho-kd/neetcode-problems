import neetcode_problems.arrays_and_hashing as ah_problems
import tests


# Stub for future tests with only one function
# arg_types = str | int | list[str] | list[int] | list[list[int]]
# result_types = bool | str | int | list[int] | list[list[str]] | None
# func_types = bool | str | list[int] | list[list[str]] | None


# def assert_test(*args: arg_types, result: result_types, func: Callable[..., func_types]):
#     assert func(*args) == result


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


@tests.pytest.mark.parametrize("nums, k, result", 
                               [([1, 1, 1, 2, 2, 3], 2, [1, 2]),
                                ([1], 1, [1])])
def test_top_k_frequent(nums: list[int], k: int, result: list[int]):
    assert ah_problems.top_k_frequent(nums, k) == result


@tests.pytest.mark.parametrize("nums, k, result", 
                               [([1, 1, 1, 2, 2, 3], 2, [1, 2]),
                                ([1], 1, [1])])
def test_top_k_frequent_counter(nums: list[int], k: int, result: list[int]):
    assert ah_problems.top_k_frequent_counter(nums, k) == result


@tests.pytest.mark.parametrize("nums, result",
                               [([1, 2, 3, 4], [24, 12, 8, 6]),
                                ([-1,1,0,-3,3], [0,0,9,0,0])])
def test_product_except_self(nums: list[int], result: list[int]):
    assert ah_problems.product_except_self(nums) == result


@tests.pytest.mark.parametrize("nums, result", 
                               [([-6, -5, -4, -3, -2, 1, 2, 3, 4], [1, 4, 4, 9, 9, 16, 16, 25, 36]),
                                ([-10000, -9999, -7, -5, 0, 0, 10000], [0, 0, 25, 49, 99980001, 100000000, 100000000]),
                                ([], [])])
def test_array_of_squares(nums: list[int], result: list[int]):
    assert ah_problems.array_of_squares(nums) == result


@tests.pytest.mark.parametrize("matrix, target, result", 
                               [([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20, False),
                                ([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5,  True)])
def test_search_matrix(matrix: list[list[int]], target: int, result: bool):
    assert ah_problems.search_matrix(matrix, target) == result


@tests.pytest.mark.parametrize("height, result", 
                               [([1,8,6,2,5,4,8,3,7], 49),
                                ([1, 1], 1)])
def test_max_area(height: list[int], result: int):
    assert ah_problems.max_area(height) == result


@tests.pytest.mark.parametrize("s, result",
                               [("III", 3),
                                ("LVIII", 58),
                                ("MCMXCIV", 1994)])
def test_roman_to_int(s: str, result: int):
    assert ah_problems.roman_to_int(s) == result


@tests.pytest.mark.parametrize("nums, result",
                               [([-2,1,-3,4,-1,2,1,-5,4], 6),
                                ([5,4,-1,7,8], 23),
                                ([-1, -1, -1, -2], -1)])
def test_max_subarray(nums: list[int], result: int):
    assert ah_problems.max_subarray(nums) == result


@tests.pytest.mark.parametrize("nums, val, result",
                               [([3,2,2,3], 3, 2),
                                ([0,1,2,2,3,0,4,2], 2, 5)])
def test_remove_element(nums: list[int], val: int, result: int):
    assert ah_problems.remove_element(nums, val) == result


@tests.pytest.mark.parametrize("nums, result", 
                               [([100,4,200,1,3,2], 4), 
                                ([0,3,7,2,5,8,4,6,0,1], 9)])
def test_longest_consecutive(nums: list[int], result: int):
    assert ah_problems.longest_consecutive(nums) == result
