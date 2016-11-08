from collections import Counter

_ = input()
print(sum(v // 2 for v in
          Counter(int(x) for x in input().strip().split()).values()))
