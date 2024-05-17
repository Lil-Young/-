# 수도 요금 경쟁 / D2

T = int(input())
for tc in range(1, T+1):
    P, Q, R, S, W = map(int, input().split())
    
    A = P*W
    B = Q if W <= R else ((W-R)*S + Q)
    price = A if A < B else B
    print(f"#{tc} {price}")