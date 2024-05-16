# 쉬운 거스름돈 / D2

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    won = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    print(f"#{tc}")
    for i in won:
        print(N//i, end=' ')
        N%=i
    print()