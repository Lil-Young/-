# N, m, M, T, R
# 시간, 초기맥박, 넘으면안되는맥박, +맥박, -맥박
# 운동을 N분하는데 필요한 시간의 최솟값
import sys
input = sys.stdin.readline
N, m, M, T, R = map(int, input().split())
init_m = m
if m+T > M: print("-1")
else:
    time, heal_time = 0, 0
    while True:
        time+=1
        if m+T <= M :
            heal_time+=1
            if heal_time == N: break
            m += T
        else:
            m -= R
        if m < init_m: m = init_m
    print(time)
    
# https://www.acmicpc.net/problem/1173