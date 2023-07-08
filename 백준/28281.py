import sys
input = sys.stdin.readline
N, X = map(int, input().split())
num = list(map(int, input().split()))
price_list = []
for i in range(N-1):
    price = num[i]*X + num[i+1]*X
    price_list.append(price)
print(min(price_list))