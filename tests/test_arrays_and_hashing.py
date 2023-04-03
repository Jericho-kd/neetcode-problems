from neetcode_problems.arrays_and_hashing import contains_duplicate

def test_contains_duplicate():
    assert contains_duplicate([1,2,3,1]) == True
    assert contains_duplicate([1,2,3,4]) == False
    assert contains_duplicate([1,1,1,3,3,4,3,2,4,2]) == True