# 홀수일까 짝수일까 / D3

T = int(input())
for tc in range(1, T+1):
    result = "Even" if int(input())%2==0 else "Odd"
    print(f"#{tc} {result}")