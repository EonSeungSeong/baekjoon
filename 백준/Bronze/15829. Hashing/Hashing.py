n = int(input())

s= input()

result =0
count =0
for i in s:
    number = ord(i)-96
    result += number *(31**count)
    count+=1
print(result)