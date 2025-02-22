"""
This module initializes the rs_enums package and exposes the Option and Some classes.
"""

from .option import Option, Some
from .result import Result, Ok, Err
from .generics import T, E

__all__ = ["Some", "Option", "Result", "Ok", "Err", "T", "E"]
