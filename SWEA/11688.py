# Calkin-Wilf tree 1 / D3

T = int(input())
for tc in range(1, T+1):
    s = input()
    a, b = 1, 1
    for pos in s:
        t = a+b
        if pos == 'L':
            b=t
        else:
            a=t
    print(f"#{tc} {a} {b}")