# import sys

# input=sys.stdin.readline
N = int(input()) 

user=[]
for i in range(N):
    age_name = list(input().split())
    user.append(age_name)
user.sort(key= lambda x: int(x[0]))
for i in range(N):
    print(user[i][0],user[i][1])