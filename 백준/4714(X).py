import sys
input = sys.stdin.readline
while True:
    a = float(input())
    if a < 0: break
    print("지구에서 무게가 {}인 물체는 달에서 무게가 {:.2f}입니다.".format(a, a*0.167))
    
# https://www.acmicpc.net/problem/4714