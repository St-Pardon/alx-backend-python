#!/usr/bin/env python3
'''Asynchronous Python
'''
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''make a list of 10 num from imported generator
    '''
    return [num async for num in async_generator()]
