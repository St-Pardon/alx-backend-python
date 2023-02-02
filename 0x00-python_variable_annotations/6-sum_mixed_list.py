#!/usr/bin/env python3
'''
type-annotated function
'''


def sum_mixed_list(mxd_lst: list[int, float]) -> float:
    '''takes mixed list return float
    '''
    return (sum(mxd_lst))
