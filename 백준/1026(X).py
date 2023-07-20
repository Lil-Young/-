import sys
input = sys.stdin.readline
num = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
sort_a = sorted(a, reverse=True)
sort_b = sorted(b)
total = 0
for i in range(num):
    total += sort_a[i]*sort_b[i]
print(total)

# https://www.acmicpc.net/problem/1026