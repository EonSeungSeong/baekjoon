n, k = map(int, input().split()) # N K 정의
li = list(map(int, input().split())) # 점수 list
li.sort(reverse=True)
print(li[k-1])
