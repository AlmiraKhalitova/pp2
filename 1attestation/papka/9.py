n = int(input())
Array = str(input()) # str
array = Array.split() #[1, 4, 3, 2, ....]
k = int(input())
str_num = str()
for i in array:
    str_num += i
x = int(str_num[0: k])

y = int(str_num[k: n])
print(x * y)