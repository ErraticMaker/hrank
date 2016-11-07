#!/bin/python3

import sys


n, k, q = tuple(int(x) for x in input().strip().split(' '))
a = [int(x) for x in input().strip().split(' ')]
for _ in range(q):
    m = int(input().strip())
    print(a[(m-k)%n])
