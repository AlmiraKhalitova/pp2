a=list(input().split())
v=[]
for i in a:
    if len(i)%2 !=0:
        v.append(i)
print(v)