from collections import deque
n= int(input())
deque=deque([s for s in range(1,n+1)])

while(len(deque)>1):
    deque.popleft()
    tmp=deque.popleft()
    deque.append(tmp)
print(deque[0])