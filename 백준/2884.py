H, M = map(int, input().split())
ToTal_mi = H*60 + M - 45
H = ToTal_mi//60
M = ToTal_mi%60
if H < 0 :
    H = H+24
print(H, M)