import neetcode_problems.trees as t_problems


def test_is_same_tree():
    assert t_problems.is_same_tree(t_problems.from_list([1, 2, 3]), 
                                   t_problems.from_list([1, 2, 3])) == True
    assert t_problems.is_same_tree(t_problems.from_list([1, 2, 3, 4, 5, 6, 7, 8]), 
                                   t_problems.from_list([1, 2, 3, 4, 5, 6, 7, 9])) == False
