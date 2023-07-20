import sys
input = sys.stdin.readline
word_list = []
for i in range(int(input())):
    word = input().rstrip()
    word_list.append(word)
word_list = set(word_list)
word_list = list(word_list)
for i in range(len(word_list)-1):
    for j in range(len(word_list)-1):
        if len(word_list[j]) > len(word_list[j+1]):
            temp = word_list[j]
            word_list[j] = word_list[j+1]
            word_list[j+1] = temp
for k in range(len(word_list)-1):
    if len(word_list[k]) == len(word_list[k+1]) and word_list[k] > word_list[k+1] :
        temp = word_list[k]
        word_list[k] = word_list[k+1]
        word_list[k+1] = temp        
print(word_list)

# https://www.acmicpc.net/problem/1181