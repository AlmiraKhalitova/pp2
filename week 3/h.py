A = list(map(int, input().split()))
min=1000
for i in A:
    if 0<i<min:
        min=i
print(min)