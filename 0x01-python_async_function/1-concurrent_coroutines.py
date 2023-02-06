#!/usr/bin/env python3
'''Asyncronus python
'''
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List:
    '''return a list of awaited response from previous function
    '''
    res: List = []
    for _ in range(n):
        res.append(await wait_random(max_delay))
    return sorted(res)
