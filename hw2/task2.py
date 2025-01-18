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
from trees import BaseBST, TreeShape


class BSTEmpty(BaseBST):
    """
    Class to represent an empty BST.
    """

    # No constructor needed

    @property
    def is_empty(self) -> bool:
        """
        Determine if a tree is empty.

        Returns (bool): True if the tree is empty, otherwise False
        """
        return True

    @property
    def is_leaf(self) -> bool:
        """
        Determine if a tree is a leaf.

        Returns (bool): True if the tree is a leaf, otherwise False
        """
        return False

    @property
    def left(self) -> BaseBST:
        """
        Get the left child of the given tree.

        Returns (BaseBST): the left child
        
        Raises: TypeError, if called on an empty tree
        """
        raise TypeError

    @property
    def right(self) -> BaseBST:
        """
        Get the right child of the given tree.

        Returns (BaseBST): the right child
        
        Raises: TypeError, if called on an empty tree
        """
        raise TypeError

    @property
    def num_nodes(self) -> int:
        """
        Get the number of nodes in the given tree.

        Returns (int): the number of nodes
        """
        return 0

    @property
    def height(self) -> int:
        """
        Get the height of the given tree.

        Returns (int): the height
        """
        return 0

    def contains(self, n: int) -> bool:
        """
        Determine if a value is in the tree.

        Inputs:
            n (int): the sought-for value

        Returns (bool): True if the value is present, otherwise False
        """
        return False

    def insert(self, n: int) -> "BSTNode":
        """
        Add a value to the tree and return the new tree.
        The original tree is returned if the value is already present.

        Inputs:
            n (int): the value to add

        Returns (BSTNode): the tree with the value added
        """
        return BSTNode(n, BSTEmpty(), BSTEmpty())

    @property
    def tree_shape(self) -> TreeShape:
        """
        Determine if a binary tree is a spine tree, zig-zag tree, or neither.
        A spine tree only has children in the same direction, where present.
        A zig-zag tree only has at most one child per node, but in either
        direction.
        A tree that is neither of these is a branching tree.
        A zero- or single-node tree is a degenerate spine tree.

        Returns (TreeShape): The type of tree detected.
        """
        raise NotImplementedError


class BSTNode(BaseBST):
    """
    Class to represent a node in a BST.
    """

    value: int
    _left: "BSTEmpty | BSTNode"
    _right: "BSTEmpty | BSTNode"

    def __init__(self, n: int, left: "BSTEmpty | BSTNode",
                               right: "BSTEmpty | BSTNode"):
        """
        Constructor

        Inputs:
            n (int): the value at this node
            left (BSTEmpty | BSTNode): the left child
            right (BSTEmpty | BSTNode): the right child

        """
        self.value = n
        self._left = left
        self._right = right

    @property
    def is_empty(self) -> bool:
        """
        Determine if a tree is empty.

        Returns (bool): True if the tree is empty, otherwise False
        """
        return False

    @property
    def is_leaf(self) -> bool:
        """
        Determine if a tree is a leaf.

        Returns (bool): True if the tree is a leaf, otherwise False
        """
        return self._left.is_empty and self._right.is_empty

    @property
    def left(self) -> BaseBST:
        """
        Get the left child of the given tree.

        Returns (BaseBST): the left child
        
        Raises: TypeError, if called on an empty tree
        """
        return self._left

    @property
    def right(self) -> BaseBST:
        """
        Get the right child of the given tree.

        Returns (BaseBST): the right child
        
        Raises: TypeError, if called on an empty tree
        """
        return self._right

    @property
    def num_nodes(self) -> int:
        """
        Get the number of nodes in the given tree.

        Returns (int): the number of nodes
        """
        return 1 + self._left.num_nodes + self._right.num_nodes

    @property
    def height(self) -> int:
        """
        Get the height of the given tree.

        Returns (int): the height
        """
        return 1 + max(self._left.height, self._right.height)

    def contains(self, n: int) -> bool:
        """
        Determine if a value is in the tree.

        Inputs:
            n (int): the sought-for value

        Returns (bool): True if the value is present, otherwise False
        """
        if n < self.value:
            return self._left.contains(n)
        elif n > self.value:
            return self._right.contains(n)
        else:
            return True

    def insert(self, n: int) -> "BSTNode":
        """
        Add a value to the tree and return the new tree.
        The original tree is returned if the value is already present.

        Inputs:
            n (int): the value to add

        Returns (BSTNode): the tree with the value added
        """
        if n < self.value:
            return BSTNode(self.value, self._left.insert(n), self._right)
        elif n > self.value:
            return BSTNode(self.value, self._left, self._right.insert(n))
        else:
            return self

    @property
    def tree_shape(self) -> TreeShape:
        """
        Determine if a binary tree is a spine tree, zig-zag tree, or neither.
        A spine tree only has children in the same direction, where present.
        A zig-zag tree only has at most one child per node, but in either
        direction.
        A tree that is neither of these is a branching tree.
        A zero- or single-node tree is a degenerate spine tree.

        Returns (TreeShape): The type of tree detected.
        """
        raise NotImplementedError

    @property
    def min(self) -> int:
        """
        Determine the minimum value in the tree.
        Exploits the BST ordering property for best efficiency.

        Returns (int): the minimum value.
        """
        raise NotImplementedError

    @property
    def max(self) -> int:
        """
        Determine the maximum value in the tree.
        Exploits the BST ordering property for best efficiency.

        Returns (int): the maximum value.
        """
        raise NotImplementedError
