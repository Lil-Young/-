# 일요일 / D3

T = int(input())
for tc in range(1, T+1):
    arr = [None, 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    s = input()
    index = arr.index(s)
    if index != 7:
        index = 7 - index
    print(f"#{tc} {index}")
