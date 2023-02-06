# 0x01. Python - Async

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2019/12/4aeaa9c3cb1f316c05c4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230206%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230206T151009Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=46e3f329df63c9fcb35b7d14c11c06fcd67df7e73daa7043eda714ce976b0ebc)

## Tasks
### [0. The basics of async](./0-basic_async_syntax.py)
Write an asynchronous coroutine that takes in an integer argument (`max_delay`, with a default value of 10) named `wait_random` that waits for a random delay between `0` and `max_delay` (included and float value) seconds and eventually returns it.

Use the `random` module.
```bash
:~$ cat 0-main.py
#!/usr/bin/env python3

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random

print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(5)))
print(asyncio.run(wait_random(15)))

:~$ ./0-main.py
9.034261504534394
1.6216525464615306
10.634589756751769
```


### [1. Let's execute multiple coroutines at the same time with async](./1-concurrent_coroutines.py)
Import `wait_random` from the previous python file that you’ve written and write an async routine called `wait_n` that takes in 2 int arguments (in this order): `n` and `max_delay`. You will spawn `wait_random` n times with the specified `max_delay`.

`wait_n` should return the list of all the delays (float values). The list of the delays should be in ascending order without using `sort()` because of concurrency.
```bash
:~$ cat 1-main.py
#!/usr/bin/env python3
'''
Test file for printing the correct output of the wait_n coroutine
'''
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n

print(asyncio.run(wait_n(5, 5)))
print(asyncio.run(wait_n(10, 7)))
print(asyncio.run(wait_n(10, 0)))

:~$ ./1-main.py
[0.9693881173832269, 1.0264573845731002, 1.7992690129519855, 3.641373003434587, 4.500011569340617]
[0.07256214141415429, 1.518551245602588, 3.355762808432721, 3.7032593997182923, 3.7796178143655546, 4.744537840582318, 5.50781365463315, 5.758942587637626, 6.109707751654879, 6.831351588271327]
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
```
The output for your answers might look a little different and that’s okay.