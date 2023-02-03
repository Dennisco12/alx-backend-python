#!/usr/bin/env python3
"""This contains an annotated function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """This returns a function"""
    return lambda x: x * multiplier
