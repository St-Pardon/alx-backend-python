# 0x00. Python - Variable Annotations

![](https://i.redd.it/y9y25tefi5401.png)

## Tasks
### [0. Basic annotations - add]()
Write a type-annotated function add that takes a float a and a float b as arguments and returns their sum as a float.
```bash
:~$ cat 0-main.py
#!/usr/bin/env python3
add = __import__('0-add').add

print(add(1.11, 2.22) == 1.11 + 2.22)
print(add.__annotations__)

:~$ ./0-main.py
True
{'a':  <class 'float'>, 'b': <class 'float'>, 'return': <class 'float'>}
```