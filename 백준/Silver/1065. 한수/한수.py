a = int(input())
count=0
for i in range(1,a+1):
    ii=str(i) #자릿수를 위한 문자열
    if i<100:
        count+=1
    elif int(ii[0])-int(ii[1]) ==int(ii[1])-int(ii[2]):
        count+=1
print(count)