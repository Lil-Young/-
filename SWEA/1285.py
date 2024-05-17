# 아름이의 돌 던지기 / D2

T = int(input())
for tc in range(1, T+1):
    people = 0
    N = int(input())
    d = list(map(int, (input().split())))
    distance = [abs(x) for x in d]
    min_value = min(distance)
    cnt = distance.count(min_value)
    print(f"#{tc} {min_value} {cnt}")