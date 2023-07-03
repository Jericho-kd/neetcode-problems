import neetcode_problems.bit_manipulation as bm_problems
import tests


@tests.pytest.mark.parametrize("nums, result", 
                               [([2,2,1], 1),
                                ([4,1,2,1,2], 4),
                                ([1], 1)])
def test_single_number(nums: list[int], result: int):
    assert bm_problems.single_number(nums) == result


@tests.pytest.mark.parametrize("n, result", 
                               [(0o00000000000000000000000000001011, 3),
                                (0o00000000000000000000000010000000, 1),
                                (0o11111111111111111111111111111101, 31)])
def test_hamming_weight(n: int, result: int):
    assert bm_problems.hamming_weight(n) == result


@tests.pytest.mark.parametrize("n, result", 
                               [(2, [0, 1, 1]),
                                (5, [0, 1, 1, 2, 1, 2])])
def test_count_bits(n: int, result: list[int]):
    assert bm_problems.count_bits(n) == result


@tests.pytest.mark.parametrize("n, result", 
                               [(43261596, 964176192), 
                                (4294967293, 3221225471)])
def test_reverse_bits(n: int, result: int):
    assert bm_problems.reverse_bits(n) == result
