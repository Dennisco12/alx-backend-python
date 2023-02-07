#!/usr/bin/env python3
"""This returns 10 random numbers"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """This collects 10 random numbers using list
    comprehension and returns them"""
    return [i async for i in async_generator()]
