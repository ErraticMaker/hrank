parse_line = lambda: (int(x) for x in input().strip().split())
t = next(parse_line())
for _ in range(t):
    _, k = tuple(parse_line())
    print('YES' if sum(1 for a in parse_line() if a <= 0) < k else 'NO')
