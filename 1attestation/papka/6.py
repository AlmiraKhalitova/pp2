count = int(input())
array = str(input()) # 2 4 3 -1 7 12 -4
list_elem = array.split()#[2, 4, 3, .....]
set_uniq = set()
for i in range(len(list_elem)):
    set_uniq.add(list_elem[i])
if len(set_uniq) == len(list_elem):
    print("YES")
else:
    print("NO")