import sys, math
input = sys.stdin.readline

# 반올림 함수
def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier

num = input().rstrip()
num = num.replace('9', '6')
if max(num) == '6':
    val = int(round_half_up(float(num.count(max(num))/2)))
    print(val)
else: print(num.count(max(num)))

# https://www.acmicpc.net/problem/1475