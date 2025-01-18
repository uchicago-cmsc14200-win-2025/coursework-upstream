#
# Base Tree classes
#
# DO NOT MODIFY THIS FILE
#

from abc import ABC, abstractmethod
from enum import Enum


TreeShape = Enum("TreeShape", ["Branching", "Spine", "ZigZag"])


class BaseBST(ABC):

    @property
    @abstractmethod
    def is_empty(self) -> bool:
        raise NotImplementedError

    @property
    @abstractmethod
    def is_leaf(self) -> bool:
        raise NotImplementedError

    @property
    @abstractmethod
    def left(self) -> "BaseBST":
        raise NotImplementedError

    @property
    @abstractmethod
    def right(self) -> "BaseBST":
        raise NotImplementedError

    @property
    @abstractmethod
    def num_nodes(self) -> int:
        raise NotImplementedError

    @property
    @abstractmethod
    def height(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def contains(self, n: int) -> bool:
        raise NotImplementedError

    @abstractmethod
    def insert(self, n: int) -> "BaseBST":
        raise NotImplementedError

    @property
    @abstractmethod
    def tree_shape(self) -> TreeShape:
        raise NotImplementedError


class RGBExpression(ABC):

    @abstractmethod
    def is_const(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def num_nodes(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def eval(self) -> tuple[int, int, int]:
        raise NotImplementedError

    @abstractmethod
    def __str__(self) -> str:
        raise NotImplementedError
