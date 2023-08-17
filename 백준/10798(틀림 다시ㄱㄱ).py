import sys
input = sys.stdin.readline
word = [input().rstrip() for _ in range(5)]
for i in range(5):
    for j in range(5):
        print(word[j][i], end = '')

# https://www.acmicpc.net/problem/10798