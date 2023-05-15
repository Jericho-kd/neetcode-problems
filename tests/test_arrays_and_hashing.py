import neetcode_problems.arrays_and_hashing as ah_problems

def test_contains_duplicate():
    assert ah_problems.contains_duplicate([1,2,3,1]) == True
    assert ah_problems.contains_duplicate([1,2,3,4]) == False
    assert ah_problems.contains_duplicate([1,1,1,3,3,4,3,2,4,2]) == True


def test_two_sum():
    assert ah_problems.two_sum([2,7,11,15], 9) == [0, 1]
    assert ah_problems.two_sum([3,2,4], 6) == [1, 2]
    assert ah_problems.two_sum([3, 3], 6) == [0, 1]


def test_is_anagram():
    assert ah_problems.is_anagram("anagram", "nagaram") == True
    assert ah_problems.is_anagram("cat", "rat") == False


def test_group_anagrams():
    #assert ah_problems.group_anagrams(["eat","tea","tan","ate","nat","bat"]) \
        #== [["bat"],["nat","tan"],["ate","eat","tea"]]
    assert  ah_problems.group_anagrams(["a"]) == [["a"]]


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
    assert ah_problems.array_of_squares([-5, -3, -1]) == [1, 9, 25]
    assert ah_problems.array_of_squares([]) == []