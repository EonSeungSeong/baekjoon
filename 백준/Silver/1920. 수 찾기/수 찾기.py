n= int(input())
lis = list(map(int, input().split()))
lis=set(lis)
m= int(input())
lis2 = list(map(int, input().split()))
for i in lis2:
    if i in lis:
        print(1)
    else:
        print(0)