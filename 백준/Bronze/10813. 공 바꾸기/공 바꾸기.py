n ,m = map(int, input().split())

lst = []
for x in range(n):
    lst.append(x+1)
    
for _ in range(m):
    i,j = map(int, input().split())
    tmp= lst[i-1]
    lst[i-1]=lst[j-1]
    lst[j-1]= tmp
for v in lst:
    print(v,end=' ')