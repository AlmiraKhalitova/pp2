sent = str(input())
sent_elem = sent.split()
lon_w = str()
len_w = int(0)

for i in sent_elem:
    if len_w < len(i):
        len_w = len(i)
        lon_w = i

print(lon_w)
print(len_w)
