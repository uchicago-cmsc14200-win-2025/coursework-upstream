"""
CMSC 14200, Winter 2025
Homework #4

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

from graph import GridGraph


def shortest_paths(
        graph: GridGraph, origin: str
) -> dict[str, tuple[int, str | None]]:
    """
    Find the shortest path from the origin to every other reacahble destination
    in the graph

    Parameters:
       graph [GridGraph]: the grid graph
       origin [str]: the starting node

    Returns dict[str, (int, str)], dict of shortest distances from origin
    to every other vertex, along with the previous vertex along the shortest
    path
    """

    # YOUR CODE HERE
    raise NotImplementedError("Task 3A")


def trace_path(
    distances: dict[str, tuple[int, str | None]], destination: str
) -> tuple[str, int]:
    """
    Given a dictionary of single-source shortest path distances and previous
    nodes, reconstruct the shortest path from source to destination

    Inputs:
       distances dict[str, (int, str)] : Shortest distance and previous nodes
       after running the shortest_paths function
       destination [str]: String label of the destination node
    Returns: tuple[str,int] : The string representing the shortest path and the 
    total distance of that path
    """

    # YOUR CODE HERE
    raise NotImplementedError("Task 3B")
