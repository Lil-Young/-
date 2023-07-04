import sys
input = sys.stdin.readline
while True :
    word = input().rstrip()
    if word == '0': break
    num = 0
    for i in word :
        if i == '1': num += 2
        elif i == '0': num += 4
        else : num += 3
    print(num + len(word) + 1)

# https://www.acmicpc.net/problem/1284