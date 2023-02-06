# 0x01. Python - Async

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2019/12/4aeaa9c3cb1f316c05c4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230206%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230206T151009Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=46e3f329df63c9fcb35b7d14c11c06fcd67df7e73daa7043eda714ce976b0ebc)

## Tasks
### [0. The basics of async]()
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