T = int(input()) #테스트 횟수

for i in range(T):
    n =int(input())
    k = int(input())
    f_0 =[x for x in range(1,k+1)]
    for j in range(n):
        for i in range(1,k):
            f_0[i]+=f_0[i-1]
    print(f_0[-1])
            
