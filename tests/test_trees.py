import neetcode_problems.trees as t_problems
from neetcode_problems.trees import from_list, to_list


def test_is_same_tree():
    assert t_problems.is_same_tree(from_list([1, 2, 3]), 
                                   from_list([1, 2, 3])) == True
    assert t_problems.is_same_tree(from_list([1, 2, 3, 4, 5, 6, 7, 8]), 
                                   from_list([1, 2, 3, 4, 5, 6, 7, 9])) == False


def test_invert_tree():
    t1_root = [4]
    t1_in = t1_root.extend(to_list(t_problems.invert_tree(from_list([4, 2, 7, 1, 3, 6, 9]))))
    t1_out = [4, 7, 2, 9, 6, 3, 1]

    t2_root = [2]
    t2_in = t2_root.extend(to_list(t_problems.invert_tree(from_list([2, 1, 3]))))
    t2_out = [2, 3, 1]

    t3_in = to_list(t_problems.invert_tree(from_list([])))
    t3_out = []

    assert t1_root == t1_out
    assert t2_root == t2_out
    assert t3_in == t3_out
