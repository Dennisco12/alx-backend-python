#!/usr/bin/env python3

"""This contains the task 0 of python async project"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """This wait for a random amount of seconds and
    returns the float amount"""
    i = random.random() * max_delay
    await asyncio.sleep(i)
    return i
