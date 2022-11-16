import math
n, k = map(int, input().split()) # N K 정의

p=1
for i in range(k):
    p*=n-i
print(p//math.factorial(k))