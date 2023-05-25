import neetcode_problems.sliding_window as sw_problems 


def test_max_profit():
    assert sw_problems.max_profit([7,1,5,3,6,4]) == 5
    assert sw_problems.max_profit_second([7,1,5,3,6,4]) == 5
    assert sw_problems.max_profit([7,6,4,3,1]) == 0
    assert sw_problems.max_profit_second([7,6,4,3,1]) == 0


def test_max_slliding_window():
    assert sw_problems.max_sliding_window([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7]
    assert sw_problems.max_sliding_window([1, -1], 1) == [1, -1]


def test_contains_nearby_duplicate():
    assert sw_problems.contains_nearby_duplicate([1,2,3,1], 3) == True
    assert sw_problems.contains_nearby_duplicate([1,0,1,1], 1) == True
    assert sw_problems.contains_nearby_duplicate([1,2,3,1,2,3], 2) == False


def test_find_max_average():
    assert sw_problems.find_max_average([1,12,-5,-6,50,3], 4) == 12.75
    assert sw_problems.find_max_average([5], 1) == 5.0
