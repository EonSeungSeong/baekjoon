n = int(input())

lst = []
for i in range(n):
    s= input()
    first =s[0]
    last = s[-1]
    f = first +last
    lst.append(f)
    
for i in range(n):
    print(lst[i])