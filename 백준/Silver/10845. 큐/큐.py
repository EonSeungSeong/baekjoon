import sys

input=sys.stdin.readline
N = int(input()) 
li=[]
for i in range(N):
    order = input().split()
    
    if order[0] =='push':
        li.append(int(order[1]))
    elif order[0] =='back':
        if len(li)==0:
            print(-1)
        else:
            print(li[-1])
            
    elif order[0] =='front':
        if len(li)==0:
            print(-1)
        else:
            print(li[0])
    
    elif order[0]=='size':
        print(len(li))
    
    elif order[0] =='pop':
        if not li:
            print(-1)
        else:
            print(li[0])
            del li[0]
    
    elif order[0] == "empty":
        if len(li)==0:
            print(1)
        else:
            print(0)