A, B, V = map(int,input().split())

height=V-A
if height%(A-B)==0:
    day=int(height/(A-B))
else:
    day=int(height/(A-B)+1)
print(day+1)