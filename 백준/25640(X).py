import sys
input = sys.stdin.readline
me = input().rstrip()
total = 0
for i in range(int(input())):
    word = input().rstrip()
    if me == word:
        total+=1
print(total)

# https://www.acmicpc.net/problem/25640