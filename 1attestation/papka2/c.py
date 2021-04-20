f, l = map(int, input().split())
cabs = list(map(int, input().split()))
ans = []
for i in range(f, l+1):
    if i not in cabs:
        ans.append(i)
print(*ans)