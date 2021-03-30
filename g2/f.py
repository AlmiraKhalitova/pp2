a, d= map(int, input().split())
cnt=0
while a<=d:
    a*=3
    d*=2
    cnt+=1
print(cnt)