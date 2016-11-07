#!/bin/python3
from functools import reduce

a = [int(x) for x in input().strip().split()]
b = [int(x) for x in input().strip().split()]
print(' '.join((str(x) for x in reduce(lambda x, y: (x[0]+y[0], x[1]+y[1]), map(lambda x: (1, 0) if x[0] > x[1] else (0, 1) if x[0] < x[1] else (0, 0), zip(a, b)), (0, 0)))))
