from collections import Counter
s=list(input().split())
s = sorted(s, key=str)
a = dict(Counter(s))
print(a)