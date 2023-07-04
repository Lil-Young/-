import sys
input = sys.stdin.readline
T = int(input())
num = list(map(int, input().split()))
N = int(input())
num_count = list(map(int, input().split()))
for i in num_count:
    print(num.count(i), end = ' ')

# https://www.acmicpc.net/problem/10816