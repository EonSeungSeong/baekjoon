n= int(input())

sum_ =0
i=0
while True:
    i+=1
    sum_+=i
    if sum_>n:
        i-=1
        break
    
print(i)