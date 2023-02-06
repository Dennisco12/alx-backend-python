#!/usr/bin/env python3
"""This takes 2 args and delay"""

from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """This spawns wait_random n times"""
    time = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
        )
    return sorted(time)
