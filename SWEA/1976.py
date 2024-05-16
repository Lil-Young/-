# 시각 덧셈 / D2

T = int(input())
for tc in range(1, T+1):
    time = list(map(int, input().split()))
    hour, minute = (time[0]+time[2]+((time[1]+time[3])//60)), (time[1]+time[3])%60
    if hour == 24:
        hour -= 12
    if hour < 24 and hour > 12:
        hour %=12
    print(f"#{tc} {hour} {minute}")