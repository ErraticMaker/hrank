#!/bin/python3

import sys
from operator import add
from functools import reduce

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
sign = ((1,0,0) if e > 0 else (0,1,0) if e < 0 else (0,0,1) for e in arr)
accu = reduce(lambda x, y: map(add, x, y), sign, (0, 0, 0))
print('\n'.join('{:0<8.6}'.format(x/len(arr)) for x in accu))
