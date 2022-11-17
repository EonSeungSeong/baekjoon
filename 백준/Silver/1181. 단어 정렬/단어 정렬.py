word_list=[]
n= int(input())
for i in range(n):
    word=input()
    word_list.append(word) #리스트 만들어줌
word_list = list(set(word_list)) #중복제거
word_list.sort()
word_list.sort(key=len)
for _ in word_list:
    print(_)

