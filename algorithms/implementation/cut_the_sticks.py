_ = input()
a = sorted([int(x) for x in input().strip().split()])
l = len(a)
print(l)
curr = a[0]
for eid, elem in enumerate(a):
    if curr != elem:
        print(l-eid)
        curr = elem
