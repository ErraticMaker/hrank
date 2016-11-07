#!/bin/python3
import sys

parse_line = lambda: (int(x) for x in input().strip().split())

start, end = tuple(parse_line())
inhouse_fruits = lambda fruits, tree: sum(1 for f in fruits
                                          if (f + tree >= start)
                                          and (f + tree <= end))

apple_tree, orange_tree = tuple(parse_line())
_ = parse_line()
print(inhouse_fruits(parse_line(), apple_tree))
print(inhouse_fruits(parse_line(), orange_tree))
