n=int(input()) # 1<=n<=1000000
lst=list(map(int,input().split())) # s,m,l,xl,xxl,xxxl
t,p = map(int,input().split())
t_bundle=0

for i in lst:
    if i==0:
        continue
    elif i<=t:
        t_bundle+=1
    elif i%t==0:
        t_bundle+=i//t
    else:
        t_bundle+=i//t+1

p_bundle=n//p
pen=n%p

print(t_bundle)
print(f'{p_bundle} {pen}')

