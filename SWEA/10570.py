# 제곱 팰린드롬 수 / D3

from math import sqrt

T = int(input())
for tc in range(1, T+1):
    total = 0
    a, b = map(int, input().split())
    for n in range(a, b+1):
        sqrt_n = sqrt(n)
        if int(sqrt_n)**2 != n:
            continue
        n, sqrt_n = list(str(n)), list(str(int(sqrt_n)))
        if n == list(reversed(n)) and sqrt_n == list(reversed(sqrt_n)):
            total+=1
    print(f"#{tc} {total}")
