num=int(input())
l = []
for i in range(num):
    a= int(input())
    l.append(a)
    l.sort()
for i in range(num):
    print(l[i])