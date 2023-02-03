#!/usr/bin/env python3
"""This contains an annotated function"""
from typing import Mapping, Any, Union, TypeVar


def safely_get_value(dct: Mapping, key: Any, default: Union[
                    TypeVar('T'), None] = None) -> Union[Any, TypeVar('T')]:
    '''function definition'''
    if key in dct:
        return dct[key]
    else:
        return default
