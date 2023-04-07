import neetcode_problems.bit_manipulation as bm_problems


def test_single_number():
    assert bm_problems.single_number([2,2,1]) == 1
    assert bm_problems.single_number([4,1,2,1,2]) == 4
    assert bm_problems.single_number([1]) == 1


def test_hamming_weight():
    assert bm_problems.hamming_weight(0o00000000000000000000000000001011) == 3
    assert bm_problems.hamming_weight(0o00000000000000000000000010000000) == 1
    assert bm_problems.hamming_weight(0o11111111111111111111111111111101) == 31


def test_count_bits():
    assert bm_problems.count_bits(2) == [0, 1, 1]
    assert bm_problems.count_bits(5) == [0, 1, 1, 2, 1, 2]


def test_reverse_bits():
    assert bm_problems.reverse_bits(43261596) == 964176192
    assert bm_problems.reverse_bits(4294967293) == 3221225471