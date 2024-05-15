# 중간 평균값 구하기 / D2

T = int(input())
for test_case in range(1, T+1):
    n = list(map(int, input().split()))
    n.sort()
    avg = int(sum(n[1:9])/8 + 0.5)
    print(f"#{test_case} {avg}")