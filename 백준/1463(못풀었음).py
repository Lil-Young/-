def is_square(x):
    if (x & (x - 1)):
        return False
    else:
        return True

import sys, math
input = sys.stdin.readline
X = int(input())
cnt = 0
while X != 1:
    if X % 2 == 0:
        X //= 2
        pass

        



# https://www.acmicpc.net/problem/1463
