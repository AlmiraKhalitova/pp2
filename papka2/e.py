n = int(input())
d = {}
while n > 0:
    inp = list(map(str, input().split()))
    if inp[0] not in d.keys():
        d[inp[0]] = inp[1:]
    else:
        for i in range(1, len(inp)):
            d[inp[0]].append(inp[i])
    n -= 1
for keys in d:
    print(keys, end=': ')
    for i, items in enumerate(d[keys], 1):
        if i == len(d[keys]):
            print(items, end='\n')
        else:
            print(items, end=', ')