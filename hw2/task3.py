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
from trees import RGBExpression


class RGBConstant(RGBExpression):
    """
    Class to represent a color constant in a color expression
    """


class Invert(RGBExpression):
    """
    Class to represent an operation that inverts a color
    """


class Blend(RGBExpression):
    """
    Class to represent a color operation that blends two colors
    """


class ChooseBrighter(RGBExpression):
    """
    Class to represent a color operation that evaluates to the brighter of two
    colors
    """
