# 숫자를 정렬하자 / D2

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))
    num.sort()
    num = [str(x) for x in num]
    print(f"#{tc} {' '.join(num)}")