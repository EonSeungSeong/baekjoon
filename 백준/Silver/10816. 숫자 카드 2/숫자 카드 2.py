from collections import Counter

N=int(input())
lst1= list(map(int,input().split()))

M=int(input())
lst2 = list(map(int,input().split()))

C=Counter(lst1)
print(" ".join(f"{C[m]}" if m in C \
               else '0' for m in lst2 ))