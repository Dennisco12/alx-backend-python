#!/usr/bin/env python3
"""This contains an annotated function"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    sum = 0
    for i in input_list:
        sum += i
    return sum
