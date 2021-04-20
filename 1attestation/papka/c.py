a=list(input().split())
b=a.copy()
b.sort()
cnt=0
for i in range(len(a)):
    if a[i]!=b[i]:
        cnt+=1
print(cnt)
