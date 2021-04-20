ids = list(input().split())
v = []
for i in ids:
    v.append(ids.count(i))
v = sorted(v, key=int)
for i in ids:
    if ids.count(i) == v[-1]:
        print(i)
        exit()