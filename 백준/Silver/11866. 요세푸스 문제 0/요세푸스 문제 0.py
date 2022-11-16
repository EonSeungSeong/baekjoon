from collections import deque
queue=deque()
ans = []
n, k = map(int, input().split())

for i in range(1,n+1):
    queue.append(i)

while queue:
    for i in range(k-1):
        queue.append(queue.popleft())
    ans.append(queue.popleft())

print("<",end='')
#print(ans)
for i in range(len(ans)-1):
    print("{}, ".format(ans[i]),end='')
print(ans[-1],end='')
print(">")