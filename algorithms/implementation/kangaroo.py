#!/bin/python3

x1, v1, x2, v2 = tuple(int(x) for x in input().strip().split())
jumps = (x2 - x1) / (v2 - v1) if (v2 - v1) != 0 else 1
print('YES' if jumps < 0 and float(int(jumps)) == jumps else 'NO')
