parse_line = lambda: (int(x) for x in input().strip().split())
_, k = tuple(parse_line())
mod = {}
for a in parse_line():
    m = a % k
    if mod.get(m) is not None:
        mod[m].append(a)
    else:
        mod[m] = [a]
c = 0
for m, v in mod.items():
    if m == 0 or m == (k - m):
        c = c + 1
    elif mod.get(k - m) is not None:
        c = c + max(len(v), len(mod[k - m])) / 2
    else:
        c = c + len(v)
print(int(c))
