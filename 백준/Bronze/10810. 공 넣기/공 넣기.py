n ,m = map(int, input().split())

lst = []
for x in range(n):
    lst.append(0)
for _ in range(m):
    i,j,k = map(int, input().split())
    for j in range(i,j+1):
        lst[j-1]=k
for v in lst:
    print(v,end=' ')