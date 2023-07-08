import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    word, a, b = input().rstrip().split()
    a = int(a); b = int(b)
    print(word[:a] + word[b:])
    
# https://www.acmicpc.net/problem/26546