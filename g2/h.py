n=int(input())
l=list(input().split())
m=int(input())
listcurrent=list(input().split())
a,b=[],[]
for i in l:
    if i not in listcurrent:
        a.append(i)
for i in listcurrent:
    if i not in l:
        b.append(i) 
print('Missed students:')
for i in a:
    print ('-', i)
    
print('Not in the group:')
for i in b:
    print ('-', i)