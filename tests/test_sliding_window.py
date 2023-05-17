import neetcode_problems.sliding_window as sw_problems 


def test_max_profit():
    assert sw_problems.max_profit([7,1,5,3,6,4]) == 5
    assert sw_problems.max_profit_second([7,1,5,3,6,4]) == 5
    assert sw_problems.max_profit([7,6,4,3,1]) == 0
    assert sw_problems.max_profit_second([7,6,4,3,1]) == 0


def test_max_slliding_window():
    assert sw_problems.max_sliding_window([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7]
    assert sw_problems.max_sliding_window([1, -1], 1) == [1, -1]