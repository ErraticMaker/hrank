#!/bin/python3

n = int(input().strip())
acc = 0
for i in range(n):
    row = [int(x) for x in input().strip().split()]
    acc = acc + row[i] - row[n-1-i]
print(abs(acc))
