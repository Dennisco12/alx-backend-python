#!/usr/bin/env python3
"""This contains a type-annotated function"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """This returns a tuple with types int and float"""
    return (k, v ** 2)
