import neetcode_problems.math_and_geometry as mg_problems

def test_plus_one():
    assert mg_problems.plus_one([1, 1, 2, 3]) == [1, 1, 2, 4]
    assert mg_problems.plus_one([9, 9]) == [1, 0, 0]
    assert mg_problems.plus_one([4, 3, 2, 1]) == [4, 3, 2, 2]


def test_is_happy():
    assert mg_problems.is_happy(19) == True
    # assert mg_problems.is_happy(2) == False # endless loop