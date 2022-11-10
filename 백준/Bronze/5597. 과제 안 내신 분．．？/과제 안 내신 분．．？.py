a=[s for s in range(1,31)]
for i in range(28):
    num=int(input())
    a.remove(num)
print(min(a))
print(max(a))