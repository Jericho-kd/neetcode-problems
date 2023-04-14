import neetcode_problems.dynamic_programming as dp_problems


def test_climb_stairs():
    assert dp_problems.climb_stairs(2) == 2
    assert dp_problems.climb_stairs(3) == 3
    assert dp_problems.climb_stairs(4) == 5