# 원재의 메모리 복구하기 / D3

T = int(input())
for tc in range(1, T+1):
    s = input()
    result = 0
    loc = '0'
    for i in s:
        if loc != i:
            loc = i
            result+=1
    print(f"#{tc} {result}")