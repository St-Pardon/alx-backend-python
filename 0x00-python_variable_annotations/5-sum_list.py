#!/usr/bin/env python3
'''
type-annotated function
'''


def sum_list(input_list: list[float]) -> float:
    '''takes list of float and reture summed value 
    '''
    res: float = 0.00
    for i in input_list:
        res += i
    return (res)
