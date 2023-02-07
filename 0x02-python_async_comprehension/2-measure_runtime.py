#!/usr/bin/env python3
'''Asynchronous Python
'''
from time import time
import asyncio


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Checks execution time
    '''
    start = time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time() - start
