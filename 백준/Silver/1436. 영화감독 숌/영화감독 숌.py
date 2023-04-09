n = int(input())

s_666=666
count=0
while True:
    if "666" in str(s_666):
        count+=1
    if count ==n:
        print(s_666)
        break
        
    s_666+=1

    