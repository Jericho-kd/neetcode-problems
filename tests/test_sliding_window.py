import neetcode_problems.sliding_window as sw_problems 


def test_max_profit():
    assert sw_problems.max_profit([7,1,5,3,6,4]) == 5
    assert sw_problems.max_profit_second([7,1,5,3,6,4]) == 5
    assert sw_problems.max_profit([7,6,4,3,1]) == 0
    assert sw_problems.max_profit_second([7,6,4,3,1]) == 0