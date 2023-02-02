#!/usr/bin/env python3
'''
type-annotated function
'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''takes list of float and reture summed value 
    '''
    res: float = 0.00
    for i in input_list:
        res += i
    return float(res)
