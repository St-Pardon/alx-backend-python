#!/usr/bin/env python3
'''Asyncronos Python
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''an asynchronous coroutine
    '''
    wait = random.random() * max_delay
    await asyncio.sleep(wait)
    return (wait)
