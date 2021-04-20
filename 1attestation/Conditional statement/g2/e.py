import re
a=list(input().split())
max=0
world=" "
for i in a:
    if len(i)>max:
        max=len(i)
        world=i
print(world)
print(max)
