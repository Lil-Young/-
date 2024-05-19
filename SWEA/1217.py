# 거듭 제곱 / D3

def func(n, m):
    if m == 1:
        return n
    return n * func(n, m-1)


for _ in range(10):
    tc = int(input())
    a, b = map(int, input().split())
    result = func(a, b)
    print(f"{tc} {result}")