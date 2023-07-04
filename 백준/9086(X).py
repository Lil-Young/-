import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    word = input().rstrip()
    print(word[0]+word[-1])

# https://www.acmicpc.net/problem/9086