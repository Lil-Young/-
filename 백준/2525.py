H, M = map(int, input().split())
T = int(input())
ToTal = H*60 + M + T
H = ToTal // 60
M = ToTal % 60
if H >= 24 :
    H = H - 24
print(H, M)