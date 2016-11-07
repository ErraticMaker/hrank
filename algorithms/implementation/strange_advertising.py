a, p = 0, 2
for _ in range(int(input().strip())):
    a, p = a + p, p * 3 // 2
print(a)
