# 10988 팰린드롬인지 확인하기

import math

text = input()
#print(len(text))

half = math.ceil(len(text) / 2)

a= []
b= []

for i in range(half):
    #print(text[i])
    a.append(text[i])
for i in range(half,0,-1):
    #print(i)
    b.append(text[-i])


if a == b[::-1]:
    print(1)
else:
    print(0)

    
