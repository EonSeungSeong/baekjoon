n ,m = map(int, input().split())

lst = []
for x in range(n):
    lst.append(x+1)
    
for _ in range(m):
    i,j = map(int, input().split())
    tmp_lst= lst[i-1:j]
    tmp_lst.reverse()
    lst[i-1:j]=tmp_lst
for v in lst:
    print(v,end=' ')