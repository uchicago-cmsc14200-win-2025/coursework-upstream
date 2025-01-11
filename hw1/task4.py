"""
CMSC 14200, Winter 2025
Homework #1, Task #4

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

from task3 import Card

def are_compatible(cards: list[Card]) -> tuple[str, str] | None:
    """
    Given a list of Card objects, determine if they are compatible.

    A set of cards is compatible if they have a single common feature
    across all of them.

    Args:
        cards: List of Card objects to check compatibility for.

    Returns: If the cards are compatible, return the common feature
       as a tuple (name, value). Otherwise, return None.
    """
    raise NotImplementedError("todo: are_compatible")
