n= int(input())

for i in range(n):
    ps=input()
    sum_ = 0
    for i in ps:
        if i == '(':
            sum_ += 1
        elif i == ')':
            sum_ -= 1
        if sum_ < 0:
            print('NO')
            break
    if sum_ > 0:
        print('NO')
    elif sum_ == 0:
        print('YES')