#
# Base graph class
#
# DO NOT MODIFY THIS FILE
#

from abc import ABC, abstractmethod

class Graph(ABC):

    @abstractmethod
    def adjacent(self, vertex: str) -> set[str]:
        """Returns the set of adjacent vertices for a given vertex; empty if
           not a vertex"""
        raise NotImplementedError

    @abstractmethod
    def is_word(self, vertex: str) -> bool:
        """Returns True if and only if the string is a word in the
           dictionary"""
        raise NotImplementedError

    @abstractmethod
    def degree(self, vertex: str) -> int:
        """Returns the degree of a given vertex; 0 if not a vertex"""
        raise NotImplementedError
