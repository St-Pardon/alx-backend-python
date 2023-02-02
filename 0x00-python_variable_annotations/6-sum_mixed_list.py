#!/usr/bin/env python3
'''
type-annotated function
'''
from typing import List


def sum_mixed_list(mxd_lst: List[int, float]) -> float:
    '''takes mixed list return float
    '''
    return (sum(mxd_lst))
