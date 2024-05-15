# 지그재그 숫자 / D2

T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    if n%2 == 0:
        print(f"#{test_case} {-(n//2)}")
    else:
        print(f"#{test_case} {n//2 + 1}")