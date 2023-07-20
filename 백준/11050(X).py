import sys
input = sys.stdin.readline
def fat(n):
    total = 1
    for i in range(n, 0, -1):
        total *= i
    return total
n, k = map(int, input().split())
result = fat(n)//(fat(n-k)*fat(k))
print(result)

# https://www.acmicpc.net/problem/11050
