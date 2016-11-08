from collections import Counter
parse_line = lambda: (int(x) for x in input().strip().split())
_, k = parse_line()
mods = Counter(a % k for a in parse_line())
print(sum(c * (mods.get((k-m) % k, 0) - (1 if m == 0 or m == k-m else 0))
          for m, c in mods.items()) // 2)
