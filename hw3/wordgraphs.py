"""
CMSC 14200, Winter 2025
Homework #3

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""
from typing import Optional
from graph import Graph


class RealWordsGraph(Graph):
    """
    Class to represent a graph over words in a language.
    Words are vertices.
    Edges connect words of the same length that are identical except at one
    letter.
    Vertices and information about adjacent vertices are explicitly stored.
    """

    def __init__(self, wordlist: str, maxlen: int):
        """
        Constructor

        Inputs:
            wordlist: name of file with words, one per line
            maxlen: ignore words longer than this
        """
        raise NotImplementedError


class PseudoWordsGraph(Graph):
    """
    Class to represent a graph over strings comprised exclusively of
    lower-case letters.
    Strings, representing pseudo-words, are vertices.
    Edges connect words of the same length that are identical except at one
    letter.
    Adjacency is determined on demand and not stored.
    """

    def __init__(self, wordlist: str):
        """
        Constructor

        Inputs:
            wordlist: name of file with words, one per line
        """
        raise NotImplementedError


class RealWordsLazyGraph(Graph):
    """
    Class to represent a graph over words in a language.
    Words are vertices.
    Edges connect words of the same length that are identical except at one
    letter.
    Adjacency is determined on demand and not stored.
    """

    def __init__(self, wordlist: str):
        """
        Constructor

        Inputs:
            wordlist: name of file with words, one per line
        """
        raise NotImplementedError


def variants(graph: Graph, start: str, distance: int) -> set[str]:
    """
    Determine the set of words in a graph the given distance away from the
    given starting vertex.

    Inputs:
        graph: the graph to traverse
        start: the starting vertex
        distance: the distance to traverse away from the starting point

    Returns: the set of vertices that distance away; empty if given string not
             a vertex
    """
    raise NotImplementedError


def shortest_word_path(
    graph: Graph, start: str, dest: str
) -> Optional[list[str]]:
    """
    Determine the shortest path between words in a graph, if a path exists.
    If there is more than one shortest path, one is chosen arbitrarily.

    Inputs:
        graph: the graph to traverse
        start: the starting vertex
        dest: the destination  vertex

    Returns: a shortest path from s to d, represented as a list whose first
             entry is s, last entry is d, and with intermediate vertices in
             order between them; None if no path exists
    """
    raise NotImplementedError
