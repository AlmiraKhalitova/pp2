set1 =set(input().split())
set2 = set(input().split())
set3= set1.intersection(set2)
print(*sorted(set3))