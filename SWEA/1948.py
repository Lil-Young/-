# 날짜 계산기

T = int(input())
for tc in range(1, T+1):
    m1, d1, m2, d2 = map(int, input().split())
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day1, day2 = 0, 0

    for i in range(0, m1-1):
        day1 += days[i]
    for i in range(0, m2-1):
        day2 += days[i]
    day1 += d1
    day2 += d2
    print(f"#{tc} {day2 - day1 + 1}")