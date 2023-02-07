#!/usr/bin/env python3
'''Asynchronous Python
'''
import random
import asyncio


async def async_generator():
    '''yeild a random number at 1sec interval 
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
