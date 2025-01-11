"""
CMSC 14200
Winter 2025

Test code for Homework #1
"""

import pytest
import task1
import task2
from tree import TreeNode

### TASK 1 TESTS ###

@pytest.mark.parametrize("list_of_dicts, expected",
                         [([{"a": 2}, {"a": 3}], {"a": 5}),
                          ([{"a": 4, "b": 1}, {"a": 5, "c": 2}], {"a": 9, "b": 1, "c": 2}),
                          ([{"b": 1}, {"c": 2}], {"b": 1, "c": 2}),
                          ([{"a": 4, "b": 1, "c": 10}, {"a": 5, "b": 20, "c": 2}], {"a": 9, "b": 21, "c": 12}),
                          ([{"a": 2, "b": 3}, {}], {"a": 2, "b": 3}),
                          ([{}, {}], {})])
def test_task1(list_of_dicts: list[dict[str, int]], expected: dict[str, int]) -> None:
    """Do a single test for Task 1: merge_dictionaries"""
    assert task1.merge_dictionaries(list_of_dicts) == expected


### TASK 2 TESTS ###

def task2_tester(tree: TreeNode, expected: list[list[int]]) -> None:
    """Test the incrementing_paths function on a given tree"""

    actual = task2.increasing_paths(tree)

    # Sort both lists to make comparison easier
    actual.sort()
    expected.sort()

    assert actual == expected

def test_task2_some_increasing() -> None:
    """
    Tests a tree where some (but not all) paths have increasing values:

        1
       / \\
      3   4
     /   / \\
    5   6   7
       / \\  \\
      1   8   3
    """

    n1 = TreeNode(1)
    n2 = TreeNode(3); n3 = TreeNode(4)
    n4 = TreeNode(5); n5 = TreeNode(6); n6 = TreeNode(7)
    n7 = TreeNode(1); n8 = TreeNode(8); n9 = TreeNode(3)

    n1.add_child(n2); n1.add_child(n3)
    n2.add_child(n4); n3.add_child(n5); n3.add_child(n6)
    n5.add_child(n7); n5.add_child(n8); n6.add_child(n9)

    task2_tester(n1, [[1, 3, 5], [1, 4, 6, 8]])

def test_task2_single_increasing() -> None:
    """
    Tests a tree with a single path with increasing values:

         3
       /   \\
      4     1
     / \\   / \\
    1   5 4   3
    """
    n1 = TreeNode(3)
    n2 = TreeNode(4); n3 = TreeNode(1)
    n4 = TreeNode(1); n5 = TreeNode(5); n6 = TreeNode(4); n7 = TreeNode(3)

    n1.add_child(n2); n1.add_child(n3)
    n2.add_child(n4); n2.add_child(n5)
    n3.add_child(n6); n3.add_child(n7)

    task2_tester(n1, [[3, 4, 5]])

def test_task2_all_increasing() -> None:
    """
    Tests a tree where every possible path has increasing values
         1
       /   \\
      2     3
     / \\   / \\
    4   5 7   9
    """
    n1 = TreeNode(1)
    n2 = TreeNode(2); n3 = TreeNode(3)
    n4 = TreeNode(4); n5 = TreeNode(5); n6 = TreeNode(7); n7 = TreeNode(9)

    n1.add_child(n2); n1.add_child(n3)
    n2.add_child(n4); n2.add_child(n5)
    n3.add_child(n6); n3.add_child(n7)

    task2_tester(n1, [[1, 2, 4], [1, 2, 5], [1, 3, 7], [1, 3, 9]])


def test_task2_none_increasing() -> None:
    """
    Tests a tree with no paths with increasing values

         10
       /   \\
      20    3
     / \\   / \\
    4   5 7   9
    """
    n1 = TreeNode(10)
    n2 = TreeNode(20); n3 = TreeNode(3)
    n4 = TreeNode(4); n5 = TreeNode(5); n6 = TreeNode(7); n7 = TreeNode(9)

    n1.add_child(n2); n1.add_child(n3)
    n2.add_child(n4); n2.add_child(n5)
    n3.add_child(n6); n3.add_child(n7)

    task2_tester(n1, [])


def test_task2_strictly_increasing() -> None:
    """
    Tests that we are looking for strictly increasing paths,
    and we did not mistakenly include paths where a value is
    equal (but not greater) than its parent's.

    We use this tree:

         1
       /   \\
      2     3
     / \\   / \\
    1   2 1   3
    """
    n1 = TreeNode(1)
    n2 = TreeNode(2); n3 = TreeNode(3)
    n4 = TreeNode(1); n5 = TreeNode(2); n6 = TreeNode(1); n7 = TreeNode(3)

    n1.add_child(n2); n1.add_child(n3)
    n2.add_child(n4); n2.add_child(n5)
    n3.add_child(n6); n3.add_child(n7)

    task2_tester(n1, [])
