import sys, math
input = sys.stdin.readline

def round_half_up(n, decimals=3):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier

N = int(input())
for i in range(N):
    total = 0
    a = list(map(int, input().split()))
    for i in range(1, len(a)) : # 점수 합
        total += a[i]
    avg = total/(len(a)-1) # 평균
    avg_over_num = 0
    for j in range(1, len(a)):
        if a[j] > avg:
            avg_over_num+=1
    result = (avg_over_num/(len(a)-1))*100
    result = round_half_up(result)
    print("{:.3f}%".format(result))
