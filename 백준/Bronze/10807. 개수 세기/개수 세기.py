num=int(input())
def count(l,n):
    count=0
    for i in range(len(l)):
        if l[i] ==n:
            count+=1
    return count

li = list(map(int, input().split()))
v = int(input())
print(count(li,v))