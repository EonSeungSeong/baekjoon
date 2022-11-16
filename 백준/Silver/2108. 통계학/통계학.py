from collections import Counter
N = int(input()) 
li=[]
for i in range(N):
    n =int(input())
    li.append(n)
li.sort()
count =Counter(li).most_common(2)

print(round(sum(li)/len(li)))
print(li[(i//2)])
if len(li)>1:
    if count[0][1]==count[1][1]:
        print(count[1][0])
    else:
        print(count[0][0])
else:
    print(count[0][0])
    
print(max(li)-min(li))