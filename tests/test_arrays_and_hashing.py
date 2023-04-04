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