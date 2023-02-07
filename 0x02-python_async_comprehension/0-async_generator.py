#!/usr/bin/env python3
"""This yield a setof random floats"""
import asyncio
from typing import List
import random


async def async_generator() -> List[float]:
    """This loops 10 times to yield a random float each time"""
    for _ in range(10):
        await asyncio.sleep(1)
        i = random.random() * 10
        yield(i)
