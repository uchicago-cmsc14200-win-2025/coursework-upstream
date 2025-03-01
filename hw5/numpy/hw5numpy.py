'''
HW5 numpy exercises (Task1 and Task2).
'''

from abc import abstractmethod, ABC
from copy import deepcopy
from typing import Any
import sys
import pandas as pd

# Task1, Task2: complete every unimplemented method in the
# classes NDArray1 and NDArray2 below

class NDArray(ABC):
    '''
    Abstract class for n-dimensional arrays.
    '''

    @property
    @abstractmethod
    def shape(self) -> int | tuple[int, int]:
        """
        Return the shape of the data, either an int (for 1d array)
        or pair of ints (for 2d array) in row, col order.
        """
        raise NotImplementedError('shape')

    @property
    @abstractmethod
    def values(self) -> list[int] | list[list[int]]:
        """
        Return the values (either a list or list of lists).
        """
        raise NotImplementedError('values')

    @abstractmethod
    def flatten(self) -> "NDArray1":
        """
        Flatten the data (either 1- or 2-dimensional)
        into a 1-dimensional array.
        """
        raise NotImplementedError('flatten')

    @abstractmethod
    def reshape(self, n: int, m: int) -> "NDArray2":
        """
        Reshape the data into an n x m array.

        Raises ValueError if the data does not have n * m elements,
        in which case the NDArray cannot be reshaped as such.
        """
        raise NotImplementedError('reshape')

# ====== Task1

class NDArray1(NDArray):
    '''
    One-dimensional arrays of integers.
    '''

    _data : list[int]
    # you can add additional attributes if you like

    def __init__(self, data: list[int]):
        """
        Construct an NDArray1 from a list of int.
        """
        self._data = deepcopy(data)

    def __pow__(self, n: int) -> 'NDArray1':
        """
        Raise every item in the array to the given power.
        Produce a new array (functional style).

        Raises ValueError if n is negative.
        """
        raise NotImplementedError('__pow__')

    def __neg__(self) -> 'NDArray1':
        """
        Negate every item in the array.
        Produce a new array (functional style).
        """
        raise NotImplementedError('__neg__')

    def __iadd__(self, n: int) -> "NDArray1":
        """
        Add n to all integers in the array, in place.
        Returns self.
        """
        raise NotImplementedError('__iadd__')

    def __isub__(self, n: int) -> "NDArray1":
        """
        Subtract n from all integers in the array, in place.
        Returns self.
        """
        raise NotImplementedError('__isub__')

    def __gt__(self, other: Any) -> list[bool]:
        """
        Return a list of bools indicating greater than given int.
        """
        raise NotImplementedError('__gt__')

    def __contains__(self, other: Any) -> bool:
        """
        Test whether the given int is in the array.
        """
        raise NotImplementedError('__contains__')

    def __eq__(self, other: Any) -> bool:
        """
        Test whether other is an NDArray1 with the same shape and
        containing the same numbers in the same positions.
        """
        raise NotImplementedError('__eq__')

    def __repr__(self) -> str:
        """
        Produce a string representation of the object.

        Note: __repr__ will not be tested or scored by us.
        It's a convenience for you during development.
        """
        raise NotImplementedError('__repr__')

    @property
    def shape(self) -> int:
        """
        see NDArray
        """
        raise NotImplementedError('shape')

    @property
    def values(self) -> list[int]:
        """
        see NDArray
        """
        raise NotImplementedError('values')

    def flatten(self) -> "NDArray1":
        """
        see NDArray
        """
        raise NotImplementedError('flatten')

    def reshape(self, n: int, m: int) -> "NDArray2":
        """
        see NDArray
        """
        raise NotImplementedError('reshape')

# ====== Task2

class NDArray2(NDArray):
    '''
    Two-dimensional arrays of integers.
    '''

    _data : list[list[int]]
    # you can add additional attributes if you like

    def __init__(self, data: list[list[int]]):
        """
        Construct an NDArray2 from a list of lists of int.

        Raises ValueError if list of lists is jagged.
        """
        self._data = deepcopy(data)

    def __pow__(self, n: int) -> "NDArray2":
        """
        Raise every item in the array to the given power.
        Produce a new array (functional style).

        Raises ValueError if n is negative.
        """
        raise NotImplementedError('__pow__')

    def __iadd__(self, n: int) -> "NDArray2":
        """
        Add n to all integers in the array, in place.
        Returns self.
        """
        raise NotImplementedError('__iadd__')

    def __isub__(self, n: int) -> 'NDArray2':
        """
        Subtract n from all integers in the array, in place.
        Returns self.
        """
        raise NotImplementedError('__isub__')

    def __neg__(self) -> 'NDArray2':
        """
        Negate every item in the array.
        Produce a new array (functional style).
        """
        raise NotImplementedError('__neg__')

    def __gt__(self, other: Any) -> list[list[bool]]:
        """
        Return a list of lists of bools indicating greater than given int.
        """
        raise NotImplementedError('__gt__')

    def __contains__(self, other: Any) -> bool:
        """
        Test whether the given int is in the array.
        """
        raise NotImplementedError('__contains__')

    def __eq__(self, other: Any) -> bool:
        """
        Test whether other is an NDArray2 with the same shape and
        containing the same numbers in the same positions.
        """
        raise NotImplementedError('__eq__')

    def __repr__(self) -> str:
        """
        Produce a string representation of the object.

        Note: __repr__ will not be tested or scored by us.
        It's a convenience for you during development.
        """
        raise NotImplementedError('__repr__')

    @property
    def shape(self) -> tuple[int, int]:
        """
        see NDArray
        """
        raise NotImplementedError('shape')

    @property
    def values(self) -> list[list[int]]:
        """
        see NDArray
        """
        raise NotImplementedError('values')

    def flatten(self) -> "NDArray1":
        """
        see NDArray
        """
        raise NotImplementedError('flatten')

    def reshape(self, n: int, m: int) -> "NDArray2":
        """
        see NDArray
        """
        raise NotImplementedError('reshape')
