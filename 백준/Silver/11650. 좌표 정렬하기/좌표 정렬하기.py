n= int(input())
xy_l=[]
for i in range(n):
    x,y = map(int, input().split())
    xy_l.append([x,y])
#print(xy_l)
xy_l.sort(key= lambda x: (x[0],x[1]))

for j in range(n):
    print(xy_l[j][0], xy_l[j][1])