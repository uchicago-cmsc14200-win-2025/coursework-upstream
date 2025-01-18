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

Coords = tuple[int, int]


class Matrix:
    """
    Class to represent a numerical matrix.

    Attributes:
        _contents (list[list[int]]): list of rows, each a list of values in row

    Methods:
        in_bounds: determine if a coordinate is within the bounds of the matrix
        get: get the value at a coordinate
        set: set the value at a coordinate
    """

    _contents: list[list[int]]

    def __init__(self, rows: int, cols: int):
        """
        Constructor for matrix with all zeros

        Inputs:
            rows (int): number of rows
            cols (int): number of columns
        """
        raise NotImplementedError

    def in_bounds(self, location: Coords) -> bool:
        """
        Determine if a coordinate is within the bounds of the matrix.

        Inputs:
            location (Coord): the (row, column) location to evaluate

        Returns (bool): True if the location is in bounds, otherwise False
        """
        raise NotImplementedError

    @property
    def rows(self) -> int:
        """
        Determine the number of rows in the matrix.

        Returns (int): The number of rows
        """
        raise NotImplementedError

    @property
    def columns(self) -> int:
        """
        Determine the number of columns in the matrix.

        Returns (int): The number of columns
        """
        raise NotImplementedError

    def get(self, location: Coords) -> int:
        """
        Gets the value at a coordinate.

        Inputs:
            location (Coord): the (row, column) location to retrieve

        Returns (int): the value at the specified location

        Raises: IndexError if location is out of bounds
        """
        raise NotImplementedError

    def set(self, location: Coords, value: int) -> None:
        """
        Sets the value at a coordinate.

        Inputs:
            location (Coord): the (row, column) location to overwrite
            value (int): the new value

        Raises: IndexError if location is out of bounds
        """
        raise NotImplementedError

    @property
    def horiz_symm(self) -> bool:
        """
        Determine if a matrix is horizontally symmetric.

        Returns (bool): True if the matrix is horizontally symmetric, otherwise
            False
        """
        raise NotImplementedError

    @property
    def vert_symm(self) -> bool:
        """
        Determine if a matrix is vertically symmetric.

        Returns (bool): True if the matrix is vertically symmetric, otherwise
            False
        """
        raise NotImplementedError

    @property
    def maj_diag_symm(self) -> bool:
        """
        Determine if a matrix is symmetric about the major diagonal.

        Returns (bool): True if the matrix is symmetric about the major
            diagonal, otherwise False
        """
        raise NotImplementedError
