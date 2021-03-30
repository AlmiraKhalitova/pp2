n = int(input())
arr = input().split()
k = int(input())

x = int('0' + ''.join(arr[:k]))
y = int('0' + ''.join(arr[k:]))

print(x*y)