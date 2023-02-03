#!/usr/bin/env python3
"""This contains an annotated function"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """This returns the sum of the list as float"""
    sums = 0.0
    for n in mxd_lst:
        sums += float(n)
    return sums
