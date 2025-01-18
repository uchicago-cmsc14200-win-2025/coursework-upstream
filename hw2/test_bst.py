"""
CMSC 14200, Winter 2025
Homework #2

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""
from task2 import TreeShape, BSTEmpty, BSTNode


def test_bst_shape_empty() -> None:
    """ Sample, already-implemented test """
    tree = BSTEmpty()
    expected = TreeShape.Spine

    actual = tree.tree_shape

    assert actual == expected


def test_bst_shape_single_node() -> None:
    """ Test a tree with a single node """
    raise NotImplementedError  # replace this line


def test_bst_shape_two_nodes_1() -> None:
    """ Test a tree with two nodes """
    raise NotImplementedError  # replace this line


def test_bst_shape_two_nodes_2() -> None:
    """ Test another tree with two nodes, but a different shape """
    raise NotImplementedError  # replace this line


def test_bst_shape_three_nodes_branching() -> None:
    """ Test a tree with three nodes, of type "branching" """
    raise NotImplementedError  # replace this line


def test_bst_shape_three_nodes_spine_1() -> None:
    """ Test a tree with three nodes, of type "spine" """
    raise NotImplementedError  # replace this line


def test_bst_shape_three_nodes_spine_2() -> None:
    """
    Test a tree with three nodes, of type "spine",
    with a different shape than the previous
    """
    raise NotImplementedError  # replace this line


def test_bst_shape_three_nodes_zigzag_1() -> None:
    """
    Test a tree with three nodes, of type "zigzag"
    """
    raise NotImplementedError  # replace this line


def test_bst_shape_three_nodes_zigzag_2() -> None:
    """
    Test a tree with three nodes, of type "zigzag",
    with a different shape than the previous
    """
    raise NotImplementedError  # replace this line


def test_bst_shape_large_branching_1() -> None:
    """ Test a tree of height at least five, of type "branching" """
    raise NotImplementedError  # replace this line


def test_bst_shape_large_branching_2() -> None:
    """
    Test a tree of height at least five, of type "branching"
    this tree should be of a different shape than the previous
    """
    raise NotImplementedError  # replace this line


def test_bst_shape_large_spine_1() -> None:
    """
    Test a tree of height at least five, of type "spine"
    """
    raise NotImplementedError  # replace this line


def test_bst_shape_large_spine_2() -> None:
    """
    Test a tree of height at least five, of type "spine"
    this tree should be of a different shape and height than the previous
    """
    raise NotImplementedError  # replace this line


def test_bst_shape_large_zigzag_1() -> None:
    """ Test a tree of height at least five, of type "zig-zag" """
    raise NotImplementedError  # replace this line


def test_bst_shape_large_zigzag_2() -> None:
    """
    Test a tree of height at least five, of type "zig-zag"
    this tree should be of a different shape and height than the previous
    """
    raise NotImplementedError  # replace this line


def test_bst_min_1() -> None:
    """
    Test a tree of height at least five.
    Each min test should use a tree with a different shape, height, and
    contents
    """
    raise NotImplementedError  # replace this line


def test_bst_min_2() -> None:
    """
    Test a tree of height at least five.
    Each min test should use a tree with a different shape, height, and
    contents
    """
    raise NotImplementedError  # replace this line


def test_bst_min_3() -> None:
    """
    Test a tree of height at least five.
    Each min test should use a tree with a different shape, height, and
    contents
    """
    raise NotImplementedError  # replace this line


def test_bst_max_1() -> None:
    """
    Test a tree of height at least five.
    Each max test should use a tree with a different shape, height, and
    contents
    """
    raise NotImplementedError  # replace this line


def test_bst_max_2() -> None:
    """
    Test a tree of height at least five.
    Each max test should use a tree with a different shape, height, and
    contents
    """
    raise NotImplementedError  # replace this line


def test_bst_max_3() -> None:
    """
    Test a tree of height at least five.
    Each max test should use a tree with a different shape, height, and
    contents
    """
    raise NotImplementedError  # replace this line
