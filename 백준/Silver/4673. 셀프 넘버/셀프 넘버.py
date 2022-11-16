range_=list(range(1,10001))
generator=[] #생성자 모아놓을 리스트
for i in range(1,10001):
    for j in str(i):
        i+=int(j)
    if i<=10000:
        generator.append(i)

for k in set(generator): #중복 다 날리기
    range_.remove(k)
for l in range_:
    print(l)
#print(generator)