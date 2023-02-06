#!/usr/bin/env python3
"""This is identical to the wait_n function"""

import asyncio
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """This spawns wait_random n times"""
    time = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
        )
    return sorted(time)
