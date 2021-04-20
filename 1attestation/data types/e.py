import math
 
terms = 10
 
a = 0
for i in range (1, terms+1):
    a += 1 / i ** 2
b = math.sqrt(6 * a)
print(b)